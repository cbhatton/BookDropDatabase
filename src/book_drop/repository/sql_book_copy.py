from typing import Optional, List

import pyodbc

from src.data_access.RecordNotFoundException import RecordNotFoundException
from conftest import reset_test_database
from src.data_access.sql_command_executor import SqlCommandExecutor
from src.book_drop.repository.i_book_copy import IBookCopyRepository


class SqlBookCopyRepository(IBookCopyRepository):

    def __init__(self, driver: str = "{SQL Server}", server: str = "", database: str = "", trusted: bool = True):
        self.executor = SqlCommandExecutor(driver=driver, server=server, database=database, trusted=trusted)

    def create_book_copy(self, name: str, author: str) -> Optional:
        if name is None or name == "":
            raise ValueError("First name cannot be empty.")
        if author is None or author == "":
            raise ValueError("Author can not be empty.")

        sp_name = "BookDrop.CreateBookCopy"
        inp_param_names = ['BookName', 'AuthorName']
        inp_param_values = [name, author]
        out_param = {
            'sp_local': ['BookID'],
            'sp_local_types': ['int'],
            'sp_out': ["BookID"]
        }

        if not self.check_for_author(author):
            self.executor.execute_stored_procedure('BookDrop.CreateAuthor',
                                                   input_param_names=['Name'],
                                                   input_param_values=[author])

        if not self.check_for_book_name(name):
            self.executor.execute_stored_procedure('BookDrop.CreateBookName',
                                                   input_param_names=['Name'],
                                                   input_param_values=[name])

        results = self.executor.execute_stored_procedure(sp_name,
                                                         input_param_names=inp_param_names,
                                                         input_param_values=inp_param_values,
                                                         output_param=out_param)

        if len(results) == 1:
            return results[0][0]
        else:
            return None

    def check_for_author(self, author):
        author = self.executor.execute_stored_procedure('BookDrop.FetchAuthor',
                                                        input_param_names=['Name'],
                                                        input_param_values=[author])

        if author[0][0] == 0:
            return False
        else:
            return True

    def check_for_book_name(self, name):
        name = self.executor.execute_stored_procedure('BookDrop.FetchBookName',
                                                      input_param_names=['Name'],
                                                      input_param_values=[name])

        if name[0][0] == 0:
            return False
        else:
            return True


if __name__ == '__main__':
    book_repo = SqlBookCopyRepository(server="(local)\\SQLEXPRESS", database="cc520")
    book_repo.create_book_copy('Dhalgren', 'Samuel Delaney')

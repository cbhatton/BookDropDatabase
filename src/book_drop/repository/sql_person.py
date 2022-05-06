from typing import Optional, List

import pyodbc

from src.data_access.RecordNotFoundException import RecordNotFoundException
from conftest import reset_test_database
from src.data_access.sql_command_executor import SqlCommandExecutor
from src.book_drop.repository.i_person import IPersonRepository
from src.book_drop.models.person import Person


class SqlPersonRepository(IPersonRepository):

    def __init__(self, driver: str = "{SQL Server}", server: str = "", database: str = "", trusted: bool = True):
        self.executor = SqlCommandExecutor(driver=driver, server=server, database=database, trusted=trusted)

    def create_person(self, name: str, user_name: str) -> Optional[Person]:
        if name is None or name == "":
            raise ValueError("First name cannot be empty.")

        sp_name = "BookDrop.CreatePerson"
        inp_param_names = ['Name', 'UserName']
        inp_param_values = [name, user_name]
        out_param = {
            'sp_local': ['PersonID'],
            'sp_local_types': ['int'],
            'sp_out': ["PersonID"]
        }

        results = self.executor.execute_stored_procedure(sp_name,
                                                         input_param_names=inp_param_names,
                                                         input_param_values=inp_param_values,
                                                         output_param=out_param)

        print(results)
        if len(results) == 1:
            return Person(results[0].PersonID_var, name)
        else:
            return None

    def retrieve_persons(self) -> Optional[List[Person]]:
        sp_name = "BookDrop.RetrievePersons"
        results = self.executor.execute_stored_procedure(sp_name)

        if len(results) >= 1:
            return results
            # return self.translate_persons(results)
        else:
            return None

    def fetch_person(self, user_name: str) -> Optional[Person]:
        sp_name = "BookDrop.FetchPerson"
        inp_param_names = ['UserName']
        inp_param_values = [user_name]

        results = self.executor.execute_stored_procedure(sp_name,
                                                         input_param_names=inp_param_names,
                                                         input_param_values=inp_param_values)
        if len(results) == 1:
            print(results)
            return results[0][0]
        else:
            raise RecordNotFoundException(user_name)

    def translate_person(self, row: pyodbc.Row) -> Person:
        return Person(row.PersonId, row.Name)

    def translate_persons(self, rows: List[pyodbc.Row]) -> List[Person]:
        persons = []
        for row in rows:
            persons.append(self.translate_person(row))
        return persons


if __name__ == "__main__":

    person_repo = SqlPersonRepository(server="(local)\\SQLEXPRESS", database="cc520")
    person = person_repo.create_person("Doug", "D_Man55")

    dougs = person_repo.retrieve_persons()
    print(dougs)

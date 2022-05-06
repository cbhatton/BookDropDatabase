from typing import Optional, List

import pyodbc

from src.data_access.RecordNotFoundException import RecordNotFoundException
from conftest import reset_test_database
from src.data_access.sql_command_executor import SqlCommandExecutor
from src.book_drop.repository.i_review import IReview
from src.book_drop.models.review_model import Review


class SqlReviewRepository(IReview):

    def __init__(self, driver: str = "{SQL Server}", server: str = "", database: str = "", trusted: bool = True):
        self.executor = SqlCommandExecutor(driver=driver, server=server, database=database, trusted=trusted)

    def create_review(self, person_id: int, book_id: int, star_rating: int, location: int) -> Optional[Review]:
        if person_id is None or not isinstance(person_id, int):
            raise ValueError("Must provide valid personID")

        sp_name = "BookDrop.CreateReview"
        inp_param_names = ['PersonID', 'BookID', 'StarRating', 'Location']
        inp_param_values = [person_id, book_id, star_rating, location]
        out_param = {
            'sp_local': ['ReviewID'],
            'sp_local_types': ['int'],
            'sp_out': ['ReviewID'],
        }

        results = self.executor.execute_stored_procedure(sp_name,
                                                         input_param_names=inp_param_names,
                                                         input_param_values=inp_param_values,
                                                         output_param=out_param)
        if len(results) == 1:
            return Review(results[0].ReviewID_var, book_id, star_rating)
        else:
            return None


if __name__ == "__main__":
    # reset_test_database()

    person_repo = SqlReviewRepository(server="(local)\\SQLEXPRESS", database="cc520")
    person = person_repo.create_review(1, 1, 4)

    # doug = person_repo.fetch_person(1)
    # print(doug.name)

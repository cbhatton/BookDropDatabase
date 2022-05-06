from src.book_drop.repository.sql_person import SqlPersonRepository
from src.book_drop.repository.sql_review import SqlReviewRepository
from src.book_drop.repository.sql_book_copy import SqlBookCopyRepository
from src.BookData import BookData

import random


class AddTestData:
    @staticmethod
    def add_books() -> None:
        books = BookData().book_data

        book_repo = SqlBookCopyRepository(server="(local)\\SQLEXPRESS", database="cc520")
        for book in books:
            book_repo.create_book_copy(book[0], book[1])

    @staticmethod
    def add_users() -> None:
        person_repo = SqlPersonRepository(server="(local)\\SQLEXPRESS", database="cc520")
        person_repo.create_person('Cody', 'justcody127')
        person_repo.create_person('Jacob', 'sneaky_lego_man')
        person_repo.create_person('Ridgely', 'TheRidge1')


    @staticmethod
    def add_reviews() -> None:
        review_repo = SqlReviewRepository(server="(local)\\SQLEXPRESS", database="cc520")

        for i in range(500):
            for user in range(1, 4):
                star_rating = random.randint(1, 5)
                book_id = random.randint(1, 363)
                location = random.randint(500, 800)

                review_repo.create_review(user, book_id, star_rating, location)


if __name__ == '__main__':
    AddTestData.add_users()
    AddTestData.add_books()
    AddTestData.add_reviews()
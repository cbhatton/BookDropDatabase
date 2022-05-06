class Book:

    def __init__(self, book_id: int, drop_id: int, author_id: int, name_id: int, review_id: int):
        self._book_id = book_id
        self._drop_id = drop_id
        self._author_id = author_id
        self._name_id = name_id
        self._review_id = review_id

    @property
    def book_id(self):
        return self._book_id

    @property
    def drop_id(self):
        return self._drop_id

    @property
    def author_id(self):
        return self._author_id

    @property
    def review_id(self):
        return self._review_id

    @property
    def name_id(self):
        return self._name_id

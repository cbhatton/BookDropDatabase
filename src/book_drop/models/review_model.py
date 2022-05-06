class Review:

    def __init__(self, review_id: int, book_id: int, star_rating):
        self._review_id = review_id
        self._book_id = book_id
        self._star_rating = star_rating

    @property
    def review_id(self):
        return self._review_id

    @property
    def book_id(self):
        return self._book_id

    @property
    def star_rating(self):
        return self._star_rating

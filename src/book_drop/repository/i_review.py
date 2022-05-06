from abc import ABC, abstractmethod
from typing import Optional, List

from src.book_drop.models.review_model import Review


class IReview(ABC):
    @abstractmethod
    def create_review(self, person_id: int, book_id: int, star_rating: int, location: int) -> Optional[Review]:
        pass

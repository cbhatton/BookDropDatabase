from abc import ABC, abstractmethod
from typing import Optional, List

from src.book_drop.models.person import Person


class IPersonRepository(ABC):
    @abstractmethod
    def create_person(self, name: str, user_name: str) -> Optional[Person]:
        pass

    @abstractmethod
    def retrieve_persons(self) -> Optional[List[Person]]:
        pass

    @abstractmethod
    def fetch_person(self, person_id: int) -> Optional[Person]:
        pass

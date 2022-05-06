from abc import ABC, abstractmethod
from typing import Optional, List


class IBookCopyRepository(ABC):
    @abstractmethod
    def create_book_copy(self, name: str, author: str) -> Optional:
        pass

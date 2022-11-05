# pylint: disable=too-few-public-methods
from typing import Dict
from abc import ABC, abstractmethod


class IDatabaseRepository(ABC):
    @abstractmethod
    def insert_artist_from_db(self, data: Dict) -> None:
        """persists data from db"""

        raise NotADirectoryError("Method not implemented!")

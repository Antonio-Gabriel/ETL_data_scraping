# pylint: disable=too-few-public-methods
from typing import Dict
from abc import ABC, abstractmethod


class IHttpRequester(ABC):
    @abstractmethod
    def request_from_page(self) -> Dict[int, str]:
        """request on archive url"""

        raise NotImplementedError("Method not implemented")

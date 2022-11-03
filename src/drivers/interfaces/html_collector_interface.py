# pylint: disable=too-few-public-methods
from typing import Dict, List
from abc import ABC


class IHtmlCollector(ABC):
    @classmethod
    def collector_essential_information(cls, html: str) -> List[Dict[str, str]]:
        """collect only essential informations"""

        raise NotImplementedError("Method not implemented")

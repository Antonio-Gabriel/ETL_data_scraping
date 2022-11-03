# pylint: disable=R0903
from typing import Dict
from requests import get


class HttpRequester:
    def __init__(self) -> None:
        self.__url = "https://web.archive.org/web/20121007172955/https://nga.gov/collection/anZ1.htm"

    def request_from_page(self) -> Dict[int, str]:
        """request on archive url"""
        response = get(self.__url, timeout=10)
        return {
            "status_code": response.status_code,
            "html": response.text
        }

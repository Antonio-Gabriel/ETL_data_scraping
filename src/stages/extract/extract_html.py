# pylint: disable=R0903
from datetime import date

from ...drivers.interfaces.http_requester_interface import IHttpRequester
from ...drivers.interfaces.html_collector_interface import IHtmlCollector

from ...errors.extract_error import ExtractError
from ..contracts.extract_contract import ExtractContract


class ExtractHtml:
    def __init__(self, http_requester: IHttpRequester, html_collector: IHtmlCollector) -> None:
        self.__http_requester = http_requester
        self.__html_collector = html_collector

    def extract(self) -> ExtractContract:
        """extract and return essential informations"""
        try:
            html_information = self.__http_requester.request_from_page()
            essential_information = self.__html_collector\
                .collector_essential_information(html_information['html'])

            return ExtractContract(
                raw_information_content=essential_information,
                extraction_date=date.today())
        except Exception as exception:
            raise ExtractError(str(exception.args)) from exception

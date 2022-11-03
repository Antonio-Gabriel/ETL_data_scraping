# pylint: disable=broad-except
from src.drivers.http_requester import HttpRequester
from src.drivers.html_collector import HtmlCollector

from .extract_html import ExtractHtml
from ...errors.extract_error import ExtractError
from ..contracts.extract_contract import ExtractContract


def test_extract():
    """test extract stage"""
    http_requester = HttpRequester()
    html_collector = HtmlCollector()

    extract_html = ExtractHtml(http_requester, html_collector)
    response = extract_html.extract()

    assert isinstance(response, ExtractContract)


def test_extract_error():
    """test extract stage fail"""
    http_requester = "It's not work"
    html_collector = HtmlCollector()

    extract_html = ExtractHtml(http_requester, html_collector)
    try:
        extract_html.extract()
    except Exception as ex:
        assert isinstance(ex, ExtractError)

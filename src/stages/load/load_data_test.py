# pylint: disable=too-few-public-methods, broad-except
from typing import Dict
from .load_data import LoadData
from ...errors.load_error import LoadError
from ..contracts.mocks.transform_contract import (
    transform_mock_contract
)
from ...infra.interfaces.database_repository_interface import (
    IDatabaseRepository
)


class RepositoryMemory(IDatabaseRepository):
    def __init__(self) -> None:
        self.artist_repository = []

    def insert_artist_from_db(self, data: Dict) -> None:
        """persists data from db"""
        self.artist_repository.append(data)


def test_load():
    """should be load data into db"""
    repo = RepositoryMemory()
    load_data = LoadData(repo)
    load_data.load(transform_mock_contract)

    assert repo.artist_repository == transform_mock_contract.load_content


def test_load_error():
    """should be fail"""
    repo = RepositoryMemory()
    load_data = LoadData(repo)

    try:
        load_data.load("It's not run")
    except Exception as ex:
        assert isinstance(ex, LoadError)

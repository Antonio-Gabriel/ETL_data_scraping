import pytest
from .database_connector import DatabaseConnector
from .database_repository import DatabaseRepository
from ..stages.contracts.mocks.transform_contract import transform_mock_contract


@pytest.mark.skip(reason="No need to insert data in database")
def test_insert_artists():
    """persists data from db test"""
    DatabaseConnector.connect()
    database_repo = DatabaseRepository()
    data = transform_mock_contract.load_content[0]
    database_repo.insert_artist_from_db(data)

from .database_connector import DatabaseConnector


def test_connector():
    """test db connection"""
    assert DatabaseConnector.connection is None
    DatabaseConnector.connect()
    assert DatabaseConnector.connection is not None

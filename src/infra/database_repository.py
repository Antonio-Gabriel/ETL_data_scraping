# pylint: disable=too-few-public-methods
from typing import Dict
from .database_connector import DatabaseConnector


class DatabaseRepository:
    @classmethod
    def insert_artist_from_db(cls, data: Dict) -> None:
        """persists data from db"""
        query = '''
            INSERT INTO artists
                (first_name, second_name, surname, artist_id, link, extraction_date)
            VALUES
                (%s, %s, %s, %s, %s, %s)
        '''

        cursor = DatabaseConnector.connection.cursor()
        cursor.execute(query, list(data.values()))

        DatabaseConnector.connection.commit()

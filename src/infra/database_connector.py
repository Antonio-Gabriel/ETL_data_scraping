# pylint: disable=too-few-public-methods
import mysql.connector as mysql


class DatabaseConnector:
    connection = None

    @classmethod
    def connect(cls):
        """mysql driver connector"""
        db_connection = mysql.connect(
            host="localhost",
            port=3306,
            database="pipeline_db",
            user="root",
            passwd=""
        )

        cls.connection = db_connection

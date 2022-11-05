# pylint: disable=too-few-public-methods
from ...errors.load_error import LoadError
from ..contracts.transform_contract import TransformContract
from ...infra.interfaces.database_repository_interface import (
    IDatabaseRepository
)


class LoadData:
    def __init__(self, repository: IDatabaseRepository) -> None:
        self.__inserted_raw: int = 0
        self.__db_repository = repository

    def load(self, transformed_data_contract: TransformContract) -> None:
        """load transformed data"""
        try:
            load_content = transformed_data_contract.load_content

            for index, data in enumerate(load_content):
                self.__inserted_raw += index
                self.__db_repository.insert_artist_from_db(data)
                print(f'Inserted rows: {str(self.__inserted_raw):#>10}')

        except Exception as exception:
            raise LoadError(str(exception)) from exception

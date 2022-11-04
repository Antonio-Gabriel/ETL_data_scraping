from .transform_raw_data import TransformRawData
from ..contracts.mocks.extract_contract import extract_contract_mock


def test_transform():
    """test for data transformation"""
    transform_raw_data = TransformRawData()
    transformed_information = transform_raw_data.transform(
        extract_contract_mock)

    print()
    print(transformed_information)

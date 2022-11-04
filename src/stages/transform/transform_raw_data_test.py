# pylint: disable=broad-except
from .transform_raw_data import TransformRawData
from ..contracts.transform_contract import TransformContract
from ..contracts.mocks.extract_contract import extract_contract_mock

from ...errors.transform_error import TransformError


def test_transform():
    """test for data transformation"""
    transform_raw_data = TransformRawData()
    transformed_data_contract = transform_raw_data.transform(
        extract_contract_mock)

    assert isinstance(transformed_data_contract, TransformContract)
    assert "first_name" in transformed_data_contract.load_content[0]


def test_transform_error():
    """should be return an error"""
    transform_raw_data = TransformRawData()

    try:
        transform_raw_data.transform("It's not run")
    except Exception as ex:
        assert isinstance(ex, TransformError)

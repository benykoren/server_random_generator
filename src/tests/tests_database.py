import sys
from os.path import abspath, dirname

import pytest

parent_dir = abspath(dirname(dirname(__file__)))
sys.path.append(parent_dir)

from database.database import DataBaseForRandoms


@pytest.fixture
def data_base_for_randoms():
    return DataBaseForRandoms()


def test_create_table_if_not_exists(data_base_for_randoms):
    result = data_base_for_randoms._create_table_if_not_exists()
    assert result is True


def test_store_random_number(data_base_for_randoms):
    result = data_base_for_randoms.store_random_number(42)
    assert result is True


def test_store_random_number_with_error(data_base_for_randoms):
    result = data_base_for_randoms.store_random_number('2')
    assert result is True


if __name__ == '__main__':
    pytest.main()

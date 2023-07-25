import sys
from os.path import abspath, dirname
from unittest.mock import MagicMock

import pytest

parent_dir = abspath(dirname(dirname(__file__)))
sys.path.append(parent_dir)

from server.random_server import RandomService


@pytest.fixture
def random_service():
    return RandomService()


def test_generate_random_number(random_service):
    request = MagicMock()
    response = random_service.AskForRandom(request, None)
    assert isinstance(response.random_number, int)


def test_store_random_number(random_service):
    random_number = 42
    random_service.data_base_for_randoms = MagicMock()
    random_service.store_random_number(random_number)
    random_service.data_base_for_randoms.store_random_number.assert_called_once_with(random_number=random_number)


if __name__ == '__main__':
    pytest.main()

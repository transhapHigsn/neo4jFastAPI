
import pytest
from src.db import get_session
from src.config import get_config

def test_dummy():
    assert 1 != 2


def test_get_session():
    session = get_session()
    assert session != None


def test_get_config():
    # fetch valid config
    neo4j_username = get_config('neo4j', 'username')
    assert neo4j_username != 'db_username'
    assert neo4j_username == 'neo4j'


@pytest.mark.xfail
def test_fetch_wrong_config():
    # fetch invalid config
    # this will fail due to KeyError
    invalid_config_val = get_config('my_secret', 'val_1')

def test_fetch_wrong_config_try_except():
    # fetch invalid config
    # this will fail due to KeyError
    try:
        invalid_config_val = get_config('my_secret', 'val_1')
    except KeyError as e:
        invalid_config_val = ''

    assert invalid_config_val == ''
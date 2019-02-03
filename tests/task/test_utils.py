from contextlib import contextmanager

import mock
import pytest

from src.task.utils import generate_id


@contextmanager
def noop():
    yield


@pytest.mark.parametrize("id_length, new_id, context_manager, expected",
                         [(4, 1234, noop(), 1234),
                          (2, 12, noop(), 12),
                          (6, None, pytest.raises(Exception), None)])
@mock.patch("random.randint")
def test_generate_id(rand_int, id_length, new_id, context_manager, expected):
    rand_int.return_value = new_id
    with context_manager:
        assert expected == generate_id(id_length)

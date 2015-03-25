from checkio_referee import RefereeBase, representations

import settings
import settings_env
from tests import TESTS

cover = """def cover(func, data):
    return func(tuple(tuple(row) for row in data[0]), data[1], data[2])
"""


def repr(data, f):
    t = data["input"]
    return "{}({}, {}, {})".format(f, tuple(tuple(row) for row in t), t[1], t[2])


class Referee(RefereeBase):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "count_neighbours"
    ENV_COVERCODE = {
        "python_2": cover,
        "python_3": cover,
        "javascript": representations.unwrap_arg_representation
    }
    CALLED_REPRESENTATIONS = {
        "python_2": repr,
        "python_3": repr,
        "javascript": None
    }

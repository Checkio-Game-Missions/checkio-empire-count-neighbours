from checkio_referee import RefereeBase, representations, covercodes, ENV_NAME


import settings_env
from tests import TESTS

cover = """def cover(func, data):
    return func(tuple(tuple(row) for row in data[0]), data[1], data[2])
"""


def repr(data, f):
    t = data["input"]
    return "{}({}, {}, {})".format(f, tuple(tuple(row) for row in t[0]), t[1], t[2])


class Referee(RefereeBase):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "count_neighbours"
    FUNCTION_NAMES = {
        ENV_NAME.JS_NODE: "countNeighbours"
    }


    ENV_COVERCODE = {
        ENV_NAME.PYTHON: cover,
        ENV_NAME.JS_NODE: covercodes.js_unwrap_args
    }
    CALLED_REPRESENTATIONS = {
        ENV_NAME.PYTHON: repr,
        ENV_NAME.JS_NODE: representations.unwrap_arg_representation()
    }

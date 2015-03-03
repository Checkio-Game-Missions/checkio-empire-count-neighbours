from checkio_referee import RefereeBase

import settings
import settings_env
from tests import TESTS

cover = """def cover(func, data):
    return func(tuple(tuple(row) for row in data[0]), data[1], data[2])
"""


class Referee(RefereeBase):
    TESTS = TESTS
    EXECUTABLE_PATH = settings.EXECUTABLE_PATH
    CURRENT_ENV = settings_env.CURRENT_ENV
    FUNCTION_NAME = "count_neighbours"
    ENV_COVERCODE = {
        "python_2": cover,
        "python_3": cover,
        "javascript": None
    }

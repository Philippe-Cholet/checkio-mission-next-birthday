from checkio import api
from checkio.signals import ON_CONNECT
from checkio.referees.io import CheckiOReferee
from checkio.referees import cover_codes

from tests import TESTS

# Date = Tuple[int, int, int]
# Args:
#     today: Date
#     birthdates: Dict[str, Date]
# Returns: It will be a list not a tuple but it doesn't matter.
#     Tuple[int, Dict[str, int]]
date_cover = '''
def cover(func, data):
    today, birthdates = data
    birthdates = {k: tuple(v) for k, v in birthdates.items()}
    return list(func(tuple(today), birthdates))
'''

api.add_listener(
    ON_CONNECT,
    CheckiOReferee(
        tests=TESTS,
        function_name={
            'python': 'next_birthday',
            'js': 'nextBirthday',
        },
        cover_code={
            'python-3': date_cover,
            'js-node': cover_codes.js_unwrap_args,
        },
    ).on_ready,
)

from datetime import MINYEAR, MAXYEAR, date
from random import randint, sample
from string import ascii_uppercase

from my_solution import next_birthday

BASIC_FAMILY = {
    'Brian': (1967, 5, 31),
    'Léna': (1970, 10, 3),
    'Philippe': (1991, 6, 15),
    'Yasmine': (1996, 2, 29),
    'Emma': (2000, 12, 25),
}

WORLD_WIDE_FAMILY = {
    'Emilie': (1990, 7, 31),
    'Jean-Baptiste': (1985, 6, 3),

    'Cameron': (1995, 11, 12),
    'Mia': (1999, 4, 5),

    'Elena': (1980, 1, 8),
    'Alexei': (1993, 10, 28),

    'Youssef': (1992, 4, 5),
    'Soraya': (1996, 12, 27),

    'Jiao': (1988, 2, 29),
    'Kang': (2012, 8, 15),

    'Pedro': (1959, 5, 2),
    'Manuela': (1961, 3, 18),

    'Inaya': (1968, 9, 22),
    'Moussa': (1976, 2, 29),
}

_today = date.today()
today = _today.year, _today.month, _today.day


def random_date(min_year: int, diff: int):
    while True:
        year = randint(min_year, min_year + diff)
        result = year, randint(1, 12), randint(1, 31)
        # Check if it is a valid date.
        try:
            date(*result)
        except ValueError:
            continue
        return result


def random_date_after(after_date, max_future: int):
    while True:
        result = random_date(after_date[0], max_future)
        if result > after_date:
            return result


def random_input(nb: int, max_range=80, max_future=20):
    """
    `nb` people that all lives within `max_range` years, and
    we look up to `max_future` years into the future.
    """
    start_year = randint(MINYEAR, MAXYEAR - max_range - max_future - 1)
    names = sample(ascii_uppercase, nb)
    births = [random_date(start_year, max_range) for _ in range(26)]
    return random_date_after(max(births), max_future), dict(zip(names, births))


# 21 tests: 3 basic, 6 world wide (today included), 12 random
TESTS = {
    '1. Basic': [
        {
            'input': ((2020, 9, 8), BASIC_FAMILY),
            'answer': (25, {'Léna': 50}),
        },
        {
            'input': ((2021, 10, 4), BASIC_FAMILY),
            'answer': (82, {'Emma': 21}),
        },
        {
            'input': ((2022, 3, 1), BASIC_FAMILY),
            'answer': (0, {'Yasmine': 26}),
        },
    ],
    '2. World Wide Family': [
        {
            'input': ((2020, 9, 8), WORLD_WIDE_FAMILY),
            'answer': (14, {'Inaya': 52}),
        },
        {
            'input': ((2013, 8, 15), WORLD_WIDE_FAMILY),
            'answer': (0, {'Kang': 1}),
            'explanation': 'Happy Birthday Kang!',
        },
        {
            'input': ((2014, 3, 29), WORLD_WIDE_FAMILY),
            'answer': (7, {'Mia': 15, 'Youssef': 22}),
            'explanation': 'Two birthdays on April 5th.',
        },
        {
            'input': ((2024, 2, 29), WORLD_WIDE_FAMILY),
            'answer': (0, {'Jiao': 36, 'Moussa': 48}),
            'explanation': 'Two birthdays on February 29th.',
        },
        {
            'input': ((2025, 3, 1), WORLD_WIDE_FAMILY),
            'answer': (0, {'Jiao': 37, 'Moussa': 49}),
            'explanation': 'Two birthdays on February 29th, '
                           'reported to March 1st.',
        },
        {
            'input': (today, WORLD_WIDE_FAMILY),
            'answer': next_birthday(today, WORLD_WIDE_FAMILY),
            'explanation': 'Today.',
        },
    ],
    '3. Random': [
        {'input': data, 'answer': next_birthday(*data)}
        for data in map(random_input, range(3, 27, 2))
    ],
}

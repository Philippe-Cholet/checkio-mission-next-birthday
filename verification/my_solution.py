from datetime import date


def next_birthday(day, births):
    # assert births, 'No data...'
    remaining_days = float('inf')
    # Convert tuples to dates.
    today = date(*day)
    for name, birth in births.items():
        birthdate = date(*birth)
        # assert today >= birthdate, f'{name} is not born yet!'
        # Find the next birthday of `name`.
        for year in (today.year, today.year + 1):
            try:
                birthday = birthdate.replace(year=year)
            except ValueError:
                # If "February 29th" does not exists then it is "March 1st".
                try:
                    birthday = date(year, 3, 1)
                except ValueError:
                    print(day, births)
                    raise
            if birthday >= today:
                break
        days = (birthday - today).days
        if days < remaining_days:
            remaining_days, ages = days, {}
        if days == remaining_days:
            ages[name] = birthday.year - birthdate.year
    return remaining_days, ages

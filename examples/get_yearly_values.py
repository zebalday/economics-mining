import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from classes.economics import API

api = API()

# Correct indicator & date format.
value = api.indicator_year(
    indicator = "BTC",
    year = 2024
)

print(value)

# Incorrect indicator falls to default [UF].
value = api.indicator_year(
    indicator = "dummy",
    year = 2024
)

print(value)

# Incorrect year falls to current year.
value = api.indicator_year(
    indicator = "BTC",
    year = 9999
)

print(value)
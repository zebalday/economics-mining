import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from classes.economics import API

api = API()

# Correct indicator & date format.
value = api.indicator_day(
    indicator = "BTC",
    date = "10-10-2024"
)

print (value)

# Incorrect indicator falls to default [UF].
value = api.indicator_day(
    indicator = "dummy",
    date = "10-10-2024"
)

print (value)

# Incorrect date falls to default today's date [dd-mm-yyyy].
value = api.indicator_day(
    indicator = "BTC",
    date = "dummy"
)

print (value)
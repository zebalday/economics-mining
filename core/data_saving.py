# imports
import sys, os, dotenv
import pandas as pd

# load & import packages
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from classes.economics import API

# envs
dotenv.load_dotenv()
DIR_PATH = os.getenv("DIR_PATH")

# get data yearly
api = API()

indicator = "IPC"
year = 2024

data = api.indicator_year(
    indicator = indicator,
    year = year
)

# save data
file_name = f"{indicator}_{year}.csv"
path = os.path.join(DIR_PATH, file_name)

data.to_csv(
    path_or_buf = path
)

# get data
indicator = "IMC"
year = 2024

data = api.indicator_year(
    indicator = indicator,
    year = year
)

# save data
file_name = f"{indicator}_{year}.csv"
path = os.path.join(DIR_PATH, file_name)

data.to_csv(
    path_or_buf = path
)

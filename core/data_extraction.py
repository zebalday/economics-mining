from requests import get
from pandas import DataFrame
from datetime import datetime


# INDICADORES
# [uf, ivp, dolar, dolar_intercambio, euro, ipc, utm, imacec, tpm, libra_cobre, tasa_desempleo, bitcoin]

INDICATORS_DICT = {
    "UF": "uf",
    "UTM": "utm",
    "IMC": "imacec",
    "IPC": "ipc",
    "BTC": "bitcoin",
    "USD": "dolar",
    "USDI": "dolar_intercamvio",
    "EU": "euro",
    "TPM": "tpm",
    "TD": "tasa_desempleo",
    "IVP": "ivp",
    "LC": "libra_cobre",
}

INDICATORS_TUPLE = [
    ("UF", "uf"),
    ("UTM", "utm"),
    ("IMC", "imacec"),
    ("IPC", "ipc"),
    ("BTC", "bitcoin"),
    ("USD", "dolar"),
    ("USDI", "dolar_intercamvio"),
    ("EU", "euro"),
    ("TPM", "tpm"),
    ("TD", "tasa_desempleo"),
    ("IVP", "ivp"),
    ("LC", "libra_cobre"),
]



# Indicador por año
def indicator_year(
        indicator : str = None,
        year : int = None
    ) -> DataFrame | None:

    indicator = INDICATORS_DICT[indicator] if indicator else INDICATORS_DICT["UF"]
    year = year if year else datetime.now().year

    url = f"https://mindicador.cl/api/{indicator}/{year}"
    result = get(url=url)

    if result.status_code == 200:
        data = result.json()["serie"]
        return DataFrame(data=data)
    
    return None



# Valor de indicador por fecha
def indicador_day(
        indicator : str = None,
        date : str = None
    ) -> dict | None:
    
    indicator = INDICATORS_DICT[indicator] if indicator else INDICATORS_DICT["UF"]
    date = date if date else datetime.now().strftime("d%-m%-y%")
    url = f"https://mindicador.cl/api/{indicator}/{date}"

    result = get(url=url)

    if result.status_code == 200:
        result = result.json()['serie'][0]
        print (result)
        return {
            'indicator' : indicator,
            'date' : date,
            'valor' : result['valor']
        }
    
    return None



# Indicador historico desde (año)
def indicator_history(
        indicator : str = None,
        year : int = None
    ) -> DataFrame | None:


    indicator = INDICATORS_DICT[indicator] if indicator else INDICATORS_DICT["UF"]
    year = year if year else datetime.now().year
    url = f"https://mindicador.cl/api/{indicator}/{year}"

    valid_year = year <= datetime.now().year


    match valid_year:

        case True:
            data = []

            if year == datetime.now().year:
                result = get(url=url)
                if result.status_code == 200:
                    data += result.json()['serie']

            else:
                for year in range(year, datetime.now().year):
                    result = get(url=url)
                    if result.status_code == 200:
                        data += result.json()['serie']
                
            return DataFrame(data=data)

        case False:
            return None
        
        case _:
            return None

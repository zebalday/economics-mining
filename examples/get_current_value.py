import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from classes.economics import API

api = API()

print(api.indicator_current("IMC"))
print(api.indicator_current("BTC"))
print(api.indicator_current("USD"))
print(api.indicator_current("TPM"))
print(api.indicator_current("IPC"))
print(api.indicator_current("IVP"))
print(api.indicator_current("UTM"))
print(api.indicator_current("EU"))
print(api.indicator_current("TD"))
print(api.indicator_current("USDI"))


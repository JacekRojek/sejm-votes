import requests
import pandas as pd

headers = {
    'accept': 'application/json',
}

response = requests.get('http://api.sejm.gov.pl/sejm/term9/MP', headers=headers).json()
deputies = pd.DataFrame.from_dict(response)
print(deputies)
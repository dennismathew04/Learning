import urllib3
from bs4 import BeautifulSoup
import pandas as pd
import json

def get_clp_places(url):
    http = urllib3.PoolManager()
    json_url = http.request('GET', url)
    data = json.loads(json_url.read())
    df = pd.json_normalize(data)
    return df

df_clp = get_clp_places("https://ecgplacesmw.colruytgroup.com/ecgplacesmw/v3/nl/places/filter/clp-places")
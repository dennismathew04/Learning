import pandas as pd
import json
from urllib.request import urlopen

def get_clp_places(url):
    json_url = urlopen(url)
    data = json.loads(json_url.read())
    df = pd.json_normalize(data)
    return df

df_clp = get_clp_places("https://ecgplacesmw.colruytgroup.com/ecgplacesmw/v3/nl/places/filter/clp-places")
print(df_clp.columns)
#a=df_clp.loc[:,'geoCoordinates.latitude']
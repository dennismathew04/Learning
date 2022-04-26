import pandas as pd
import json
from urllib.request import urlopen
import unittest

def get_clp_places(url):
    json_url = urlopen(url)
    data = json.loads(json_url.read())
    df = pd.json_normalize(data)
    return df

df_clp = get_clp_places("https://ecgplacesmw.colruytgroup.com/ecgplacesmw/v3/nl/places/filter/clp-places")

tc=unittest.TestCase('__init__')
tc.assertGreater(len(df_clp.index),200,'Record count is less than 200')
tc.assertTrue(df_clp['geoCoordinates.latitude'].min()>49 and df_clp['geoCoordinates.latitude'].max()<52,'Latitude is not within 49 and 52')
tc.assertTrue(df_clp['geoCoordinates.longitude'].min()>2 and df_clp['geoCoordinates.longitude'].max()<7,'longitude is not within 2 and 7')

df_clp['antwerpen']= df_clp['address.cityName'].apply(lambda y: '1' if 'ANTWERPEN' in y.upper() else '0')




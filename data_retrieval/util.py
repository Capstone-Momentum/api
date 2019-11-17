
import pandas as pd
import urllib3 as url3
import json

def get(url):
    http = url3.PoolManager()
    resp = http.request('GET', url)
    return json.loads(resp.data)

def getDataFrame(url):
    return pd.DataFrame(get(url))


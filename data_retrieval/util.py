
import pandas as pd
import urllib3 as url3
import json

# Documenting with this style: https://docs.python-guide.org/writing/documentation/

def get(url):
    """
    Performs a GET request and returns the data as a dictionary.

    Assumes the response data is in JSON.

    Parameters
    ----------
    url : str
        The full url (base + endpoint)

    Returns
    -------
    dict
        The response data

    """
    http = url3.PoolManager()
    resp = http.request('GET', url)
    return json.loads(resp.data)

def getDataFrame(url):
    """
    Performs a GET request and returns the data as a pandas DataFrame.

    Parameters
    ----------
    url : str
        The full url (base + endpoint)

    Returns
    -------
    pandas.DataFrame
        The response data

    """
    return pd.DataFrame(get(url))


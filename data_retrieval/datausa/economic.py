
import pandas as pd
import seaborn as sns
import urllib3 as url
import json

# Link to SLO County Summary: https://datausa.io/profile/geo/san-luis-obispo-county-ca

def getDataFrame(route):
    http = url.PoolManager()
    resp = http.request('GET', route)
    data = json.loads(resp.data)['data']
    return pd.DataFrame(data)

def test():
    df = getDataFrame(
        'http://datausa.io/api/data?Geography=05000US06079:children&measure=Household Income by Race,Household Income by Race Moe&Race=0')
    print(df)
    sns.catplot(x="Household Income by Race", y="Geography", kind="swarm", data=df.sample(15))
    df = getDataFrame('http://datausa.io/api/data?geo=05000US06079&measure=Average%20Wage,Average%20Wage%20Appx%20MOE,Total%20Population,Total%20Population%20MOE%20Appx,Record%20Count&drilldowns=Gender&Employment%20Time%20Status=1&Detailed%20Occupation=119XXX,412010,412031,252020,533030&Record%20Count>=5')
    print(df)
    sns.catplot(x="Gender", y="Average Wage", hue="Detailed Occupation", kind="bar", data=df)


if __name__ == '__main__':
    test()

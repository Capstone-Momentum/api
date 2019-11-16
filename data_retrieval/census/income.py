
import bs4
import pandas as pd
import urllib3 as url
import json

# API Key: 59b58e145abf5f84f347813e3e52cca496db9a0f
# Available data summary: https://www.census.gov/data/developers/guidance/api-user-guide.Available_Data.html
# Query Components: https://www.census.gov/data/developers/guidance/api-user-guide.Query_Components.html
# Census data api overview: https://www.census.gov/data/developers/guidance/api-user-guide.html
# Population Estimates APIs: https://www.census.gov/data/developers/data-sets/popest-popproj/popest.html

# census.gov's FTP root: https://www2.census.gov/

# ACS Table Shells: https://www2.census.gov/programs-surveys/acs/tech_docs/table_shells/2018/?#
# ACS Table IDs Explained: https://www.census.gov/programs-surveys/acs/guidance/which-data-tool/table-ids-explained.html
# ACS Variables (2018): https://api.census.gov/data/2018/acs/acs1/variables.html

'''
County Codes for California: https://www2.census.gov/geo/pvs/sdrp/2020annotation/st06_ca/06_County_Coverage_A.txt

06         079         San Luis Obispo                      00009 Cuyama Joint Unified School District                                                                
06         079         San Luis Obispo                      00048 Paso Robles Joint Unified School District                                                           
06         079         San Luis Obispo                      00049 Coast Unified School District                                                                       
06         079         San Luis Obispo                      03300 Atascadero Unified School District                                                                  
06         079         San Luis Obispo                      07840 Cayucos Elementary School District                                                                  
06         079         San Luis Obispo                      23080 Lucia Mar Unified School District                                                                   
06         079         San Luis Obispo                      31020 Pleasant Valley Joint Union Elementary School District                                              
06         079         San Luis Obispo                      34800 San Luis Coastal Unified School District                                                            
06         079         San Luis Obispo                      35010 San Miguel Joint Union Elementary School District                                                   
06         079         San Luis Obispo                      36450 Shandon Joint Unified School District                                                               
06         079         San Luis Obispo                      39000 Templeton Unified School District                                                                   
06         079         San Luis Obispo                      99009 Coast Unified School District (9-12)                                                                
06         079         San Luis Obispo                      99010 Paso Robles Joint Unified School District (9-12)                                                    
'''

'''
Narrowing Queries to Geography:

The predicate &for restricts the variables by geography at various levels, while &in and + restricts to geographic areas smaller than state level. You can include wildcards (:*) along with &for and &in.

Examples:

&for=state:01 – restricts the result to include only Alabama
&for=county:001&in=state:01 – restricts the result to include only Autauga County, Alabama
&for=county:073&in=state:01+place:07000 – restricts the result to include the portion of Jefferson County (county:073), Alabama that is within Birmingham city (place:07000)
Examples with wildcards:

&for=state:* – retrieves the result for all states
&for=county:*&in=state:01 – restricts the result to include all counties in Alabama
&for=county:*&in=state:01+place:62328 – restricts the result to include all counties within Prattville city (place: 62328), Alabama
'''

# Setup an AWS Lambda to run on a schedule: https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/RunLambdaSchedule.html

def getDataFrame(endpoint):
    http = url.PoolManager()
    resp = http.request('GET', endpoint)
    data = json.loads(resp.data)
    return pd.DataFrame(data)

def testing_census_api(year, vars):
    baseUrl = "https://api.census.gov/data/{}/acs/acs1".format(str(year))
    varsStr = ",".join(vars)
    tests = [
        ('all_states', "{}?get=NAME,{}&for=state:*".format(baseUrl, varsStr)),
        ('california', "{}?get=NAME,{}&for=state:06".format(baseUrl, varsStr)),
        ('slo', "{}?get=NAME,{}&for=county:079&in=state:06".format(baseUrl, varsStr))
    ]
    for test in tests:
        label, endpoint = test
        summarize(label, getDataFrame(endpoint))

def summarize(header, df):
    summary = "\n\n{}:\n\n{}".format(header, str(df))
    print(summary)

if __name__ == '__main__':
    testing_census_api(2018, ['B11001C_005E'])

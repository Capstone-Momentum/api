
import traceback
import sys
import boto3
import json
from data_retrieval.util import get
from data_retrieval.census.constants import VARIABLES_TABLE_NAME_BASE
from data_retrieval.census.create_tables import get_table_name

'''
Retrieving/Storing variable definitions (Pseudo):
    1. define base url
    2. for each year, add it to the url, and do the following on that page
        - for each table/profile type (detailed, subject, data profile, comparison profile, selected population profile)
            - retrieve the json definition of the variables
            - store these in a db table specific to the year and table

Retrieving/Storing the actual data (Pseudo):
    1. for each year we have variables
        - create a db table to hold that year's data (maybe a separate table corresponding to each table/profile type in the census' schema)
        - for each variable
            - query the census api for its data and store it in our newly created db table
'''

def scrape_variable_definitions(year, acs_table_type=''):
    """
    Scrapes the ACS variable definitions and puts them into a dynamoDB table.

    Parameters
    ----------
    year : int
        the ACS year to scrape for
    var_option : str
        one of... subject, profile, cprofile, spp, or the default '' which accesses the 'Detailed Tables'
    """
    baseUrl = "https://api.census.gov/data/{}/acs/acs1/{}variables.json".format(str(year), "{}/".format(acs_table_type) if (acs_table_type) else acs_table_type)

    # get the variables
    vars = get(baseUrl)['variables']
    varsKeys = list(vars.keys())

    # gain connection to the correct table
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(get_table_name(year, acs_table_type))

    # insert into the db in batches to minimize the number of requests
    batch_size = 5
    for batch_start in range(0, len(vars) - batch_size, batch_size):
        with table.batch_writer(overwrite_by_pkeys=['variable_name', 'group']) as batch:
            for item_idx in range(batch_start, batch_start + batch_size):
                var = varsKeys[item_idx]
                print(var)
                try:
                    batch.put_item(
                        Item={
                            'variable_name': var,
                            'group': vars[var]['group'],
                            'label': vars[var]['label'],
                            'concept': vars[var]['concept'],
                            'attributes': vars[var]['attributes'].split(','),
                        }
                    )
                except:
                    traceback.print_exc()
                    print(var, file=sys.stderr)
                    print(json.dumps(vars[var], indent=4), file=sys.stderr)
        print('Attempted adding {} variables'.format(str(batch_start)))

def scrape_data():
    pass

if __name__ == '__main__':
    scrape_variable_definitions(2018)


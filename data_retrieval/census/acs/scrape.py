
import datetime
import traceback
import sys
import json
from boto3_wrapper.dynamodb import get_table
from data_retrieval.util import get
from data_retrieval.census.acs.create_tables import get_table_name
from constants.census.constants import ACS_TABLE_TYPES_PRE_2016, ACSTableItem, API_KEY

'''
This module holds the logic for scraping ACS (American Community Survey)

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

def scrape_acs_table_on_year(acs_table_type, year):
    """
    Scrapes the ACS variable definitions and puts them into a dynamoDB table.

    Parameters
    ----------
    acs_table_type : str
        one of... subject, profile, cprofile, spp, or the default '' which accesses the 'Detailed Tables'
    year : int
        the ACS year to scrape for
    """
    baseUrl = "https://api.census.gov/data/{}/acs/acs1".format(str(year))
    tableVariablesUrl = "{}/{}variables.json".format(baseUrl, "{}/".format(acs_table_type) if (acs_table_type) else acs_table_type)
    print('Starting: {}'.format(baseUrl))

    # get the variables
    vars = get(tableVariablesUrl)['variables']
    print('{} variables to add'.format(str(len(vars))))
    varsKeys = list(vars.keys())

    # gain connection to the correct table
    table = get_table(get_table_name(acs_table_type))
    startTime = datetime.datetime.now()

    # insert into the db in batches to minimize the number of requests (max batch size is 5 for AWS Free Tier)
    batch_size = 5
    num_items_added = 0
    for batch_start in range(0, len(vars) - batch_size, batch_size):
        with table.batch_writer(overwrite_by_pkeys=[ACSTableItem.VARIABLE_NAME.value, ACSTableItem.YEAR.value]) as batch:
            for item_idx in range(batch_start, batch_start + batch_size):
                var = varsKeys[item_idx]

                # Fill in missing attributes to keep table schemas consistent
                varAttrs = vars[var].keys()
                for attr in [ACSTableItem.GROUP.value, ACSTableItem.LABEL.value, ACSTableItem.CONCEPT.value, ACSTableItem.CALIFORNIA.value, ACSTableItem.SLO_COUNTY.value]:
                    if (attr not in varAttrs):
                        vars[var][attr] = None
                vars[var]['attributes'] = vars[var]['attributes'].split(',') if ('attributes' in varAttrs) else None
                # trim group name if it's too long (1024 is the max characters for a 'sort key' in AWS)
                vars[var]['group'] = vars[var]['group'] if (vars[var]['group'] is not None and len(vars[var]['group']) <= 1024) else vars[var]['group'][:1024]

                # retrieve the values for this variable (california and slo county)
                try:
                    californiaValue = get("{}?get={}&for=state:06&key={}".format(baseUrl, var, API_KEY))[1][0]
                except:
                    californiaValue = None
                try:
                    sloCountyValue = get("{}?get={}&for=county:079&in=state:06&key={}".format(baseUrl, var, API_KEY))[1][0]
                except:
                    sloCountyValue = None

                try:
                    batch.put_item(
                        Item={
                            ACSTableItem.VARIABLE_NAME.value: var,
                            ACSTableItem.GROUP.value: vars[var]['group'],
                            ACSTableItem.YEAR.value: year,
                            ACSTableItem.LABEL.value: vars[var]['label'],
                            ACSTableItem.CONCEPT.value: vars[var]['concept'],
                            ACSTableItem.ATTRIBUTES.value: vars[var]['attributes'],
                            ACSTableItem.CALIFORNIA.value: californiaValue,
                            ACSTableItem.SLO_COUNTY.value: sloCountyValue,
                        }
                    )
                    num_items_added += 1
                except:
                    try:
                        traceback.print_exc()
                        print(var, file=sys.stderr)
                        print(json.dumps(vars[var], indent=6), file=sys.stderr)
                    except:
                        continue
        if (num_items_added % 100 == 0):
            print('{} items added, total time elapsed: {:.2f} minutes'.format(str(num_items_added), (datetime.datetime.now() - startTime).total_seconds() / 60))

def scrape_acs():
    # for year in ACS_YEARS[5:]:
    #     for tableType in ACS_TABLE_TYPES:
    #         scrape_acs_table_on_year(tableType, year)
    for tableType in ACS_TABLE_TYPES_PRE_2016:
        scrape_acs_table_on_year(tableType, 2014)

if __name__ == '__main__':
    scrape_acs()











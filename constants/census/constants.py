
from enum import Enum

# This is free and took like 2 minutes to get from the census website so don't feel like we need to use an environment variable
API_KEY = "59b58e145abf5f84f347813e3e52cca496db9a0f"

ACS_TABLE_NAME_BASE = 'census_acs1'
ACS_TABLE_TYPES_PRE_2016 = ['', 'subject', 'profile', 'cprofile']
ACS_TABLE_TYPES = ['', 'subject', 'profile', 'cprofile', 'spp']
ACS_YEARS = list(range(2011, 2019))

# ACS Table Item Attributes
class ACSTableItem(Enum):
    VARIABLE_NAME = 'variable_name'
    GROUP = 'group'
    YEAR = 'year'
    LABEL = 'label'
    CONCEPT = 'concept'
    ATTRIBUTES = 'attributes'
    CALIFORNIA = 'california'
    SLO_COUNTY = 'slo_county'

# Datasets Table Item Attributes
class DatasetItem(Enum):
    TITLE = 'title'
    DATASETNAMES = 'dataset_names'
    DESCRIPTION = 'description'
    VINTAGE = 'vintage'
    GEOGRAPHY_LINK = 'geography_link'
    GROUPS_LINK = 'groups_link'
    SOURCE_PATH = 'source_path'


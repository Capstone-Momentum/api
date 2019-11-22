
from boto3_wrapper.dynamodb import get_table
from constants.census.constants import DatasetItem

def define_data_sources():
    table = get_table('data_sources')
    table.put_item(
        Item={
            'name': 'Census',
            'description': 'Once a decade, America comes together to count every resident in the United States, creating national awareness of the importance of the census and its valuable statistics. The decennial census was first taken in 1790, as mandated by the Constitution. It counts our population and households, providing the basis for reapportioning congressional seats, redistricting, and distributing more than $675 billion in federal funds annually to support states, counties and communities’ vital programs — impacting housing, education, transportation, employment, health care and public policy.',
            'associated_tables': ['census_datasets']
        }
    )


if __name__ == '__main__':
    define_data_sources()


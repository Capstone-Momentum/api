
from boto3_wrapper.dynamodb import get_table
from data_retrieval.util import get
from constants.census.constants import DatasetItem, API_KEY

def scrape_dataset_definitions():
    url = 'https://api.census.gov/data.json'
    datasets = get(url)['dataset']
    table = get_table('census_datasets')
    for dataset in datasets:
        print(dataset)
        try:
            table.put_item(
                Item={
                    DatasetItem.TITLE.value: dataset['title'],
                    DatasetItem.DATASETNAMES.value: "-".join(dataset['c_dataset']),
                    DatasetItem.DESCRIPTION.value: dataset['description'],
                    DatasetItem.VINTAGE.value: dataset['c_vintage'],
                    DatasetItem.GEOGRAPHY_LINK.value: dataset['c_geographyLink'],
                    DatasetItem.VARIABLES_LINK.value: dataset['c_variablesLink'],
                    DatasetItem.GROUPS_LINK.value: dataset['c_groupsLink'],
                    DatasetItem.SOURCE_PATH.value: dataset['distribution'][0]['accessURL'].split('/')[5:]
                }
            )
        except Exception as e:
            print(e)

if __name__ == '__main__':
    scrape_dataset_definitions()


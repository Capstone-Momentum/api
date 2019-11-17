
import bs4

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

def scrape():
    pass

if __name__ == '__main__':
    scrape()


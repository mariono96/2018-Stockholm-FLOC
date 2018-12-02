from hdx.hdx_configuration import Configuration
from hdx.data.dataset import Dataset
from hdx.location.country import Country
import os

# Setup hdx access
conf = Configuration.create(hdx_site='prod', user_agent='A_Quick_Example', hdx_read_only=True, project_config_dict = {})
# Search for datasets with the keyword we want
datasets = Dataset.search_in_hdx('Requirements and Funding Data', rows=800)
# Get a list of the names of the actual csv-files
resources = Dataset.get_all_resources(datasets)
# Get all the three-digit country codes
africaCodes = [x.lower() for x in Country.get_countries_in_region('Africa')]

# Delete current files before getting new versions
filelist = [ f for f in os.listdir("csv") if f.endswith(".CSV") ]
for f in filelist:
    os.remove(os.path.join("csv", f))

# Download all the files that match the naming pattern of the files we want
for resource in resources:
    for countryCode in africaCodes:
        if "fts_requirements_funding_" + countryCode + ".csv" == resource['name']:
            resource.download('csv')

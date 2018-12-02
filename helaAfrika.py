from hdx.utilities.easy_logging import setup_logging
from hdx.hdx_configuration import Configuration
from hdx.data.dataset import Dataset
from hdx.location.country import Country

setup_logging()

conf = Configuration.create(hdx_site='prod', user_agent='A_Quick_Example', hdx_read_only=True, project_config_dict = {})
datasets = Dataset.search_in_hdx('Requirements and Funding Data', rows=800)

resources = Dataset.get_all_resources(datasets)
africaCodes = [x.lower() for x in Country.get_countries_in_region('Africa')]
toDownload = []

for resource in resources:
    for countryCode in africaCodes:
        if "fts_requirements_funding_" + countryCode + ".csv" == resource['name']:
            #toDownload.append(resource['name'])
            resource.download('csv')

print("TO DOWNLOAD:")
for name in toDownload:
    print(name)

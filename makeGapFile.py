# NOTICE! This script assumes the correct CSV-files have been downloaded by helaAfrika.py into the csv-folder
import csv
import os
from math import log

class CountryInfo:
    def __init__(self, countryName, countryCode, requirements, funding, infoYear):
        self.countryName = countryName
        self.countryCode = countryCode
        self.requirements = requirements
        self.funding = funding
        self.infoYear = infoYear
        self.gap = requirements - funding
        self.visGap = None
    def __str__(self):
        return self.countryName + \
                "\nRequirements: " + str(self.requirements) + \
                "\nFunding: " + str(self.funding) + \
                "\nGap: " + str(self.gap)

#Create a CountryInfo-object out of a file
def extractCountryInfo(filename):
    with open(filename) as file:
        rows = []
        for row in csv.reader(file):
            rows.append(row)
        year = rows[2][6]
        countryName = rows[2][0]
        countryCode = str(filename.split("_")[3][0:3])
        requirements = int(rows[2][7])
        if rows[2][8] == "":
            funding = 0
        else:
            funding = int(rows[2][8])
    return CountryInfo(countryName, countryCode, requirements, funding, year)

#rescales the gap values for better visualisation
#makes sure values start from zero and goes all logarithmic on them
def processGaps(countries):
    #find lowest gap
    lowestGap = min(map(lambda country: country.gap, countries))
    for country in countries:
        country.visGap = log((country.gap - lowestGap) + 1)

# Create a bunch of CountryInfo objects and add them to a list
countries = []
for filename in os.listdir("csv"):
    country = extractCountryInfo("csv/" + filename)
    countries.append(country)

processGaps(countries)

# Go through the list and create the output csv-file
outputString = ""
outputString += "Country_code,Gap,Date;VisGap\n"
for country in countries:
    outputString += country.countryCode.upper() + "," + \
                    str(country.gap) + "," + \
                    country.infoYear + "," + \
                    str(country.visGap) + "\n"

outputFile = open("output.csv", "w")
outputFile.write(outputString)
outputFile.close()

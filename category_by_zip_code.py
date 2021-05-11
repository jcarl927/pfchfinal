import csv
import pprint 
import pandas as pd

category_by_zip_code_count = {}

pp = pprint.PrettyPrinter(indent=4)


with open("Film_Permits.csv", "r") as myfile:
    reader = csv.DictReader(myfile)
    for row in reader:

        #filter to just shooting permits and shooting permits on city property
        if row['EventType'] == 'Shooting Permit' or row['EventType'] == 'DCAS Prep/Shoot/Wrap Permit':

            #for every permit that has only one zip code in row['ZipCode(s)'], add the zip code to the dictionary as a key
            #and filter out zip codes that are "N/A" or "0"
            if "," not in row['ZipCode(s)']:
                single_zip_code = row['ZipCode(s)']
                if single_zip_code != '0' and single_zip_code != 'N/A':

                    #create keys for each individual zip code
                    if single_zip_code in category_by_zip_code_count:
                        pass
                    else:
                        category_by_zip_code_count[single_zip_code] = {}

                    #count instances of each category per zip code
                    category = row['Category']
                    if category in category_by_zip_code_count[single_zip_code]:
                        category_by_zip_code_count[single_zip_code][category] = category_by_zip_code_count[single_zip_code][category] + 1
                    else:
                        category_by_zip_code_count[single_zip_code][category] = 1

            #for permits that have multiple zip codes in row['ZipCode(s)'], create lists of zip codes
            if "," in row['ZipCode(s)']:
                zip_code_lists = row['ZipCode(s)'].split(", ")

                #for any zip codes that did not appear in the single zip code section, add the zip code to the dictionary as a key
                #and filter out zip codes that are "N/A" or "0"
                for zip_code in zip_code_lists:
                    if zip_code != '0' and zip_code != 'N/A':
                        if zip_code in category_by_zip_code_count:
                            pass
                        else:
                            category_by_zip_code_count[zip_code] = {}

                    #count instances of each category per zip code  
                        category = row['Category']
                        if category in category_by_zip_code_count[zip_code]:
                            category_by_zip_code_count[zip_code][category] = category_by_zip_code_count[zip_code][category] + 1
                        else:
                            category_by_zip_code_count[zip_code][category] = 1

#check that everything has worked correctly by printing the dictionary
pp.pprint(category_by_zip_code_count)


#using pandas, write the nested dictionary to a csv file for visualizing in Tableau
pd.DataFrame.from_dict(category_by_zip_code_count, orient='index').to_csv('category_by_zip_code.csv')

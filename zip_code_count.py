import csv
import pprint 

zip_code_count = {}

pp = pprint.PrettyPrinter(indent=4)

with open("Film_Permits.csv", "r") as originalcsvfile:
    reader = csv.DictReader(originalcsvfile)
    for row in reader:

        #filter to just shooting permits and shooting permits on city property
        if row['EventType'] == 'Shooting Permit' or row['EventType'] == 'DCAS Prep/Shoot/Wrap Permit':

            #get zip code count for every permit that only contains one zip code
            #and filter out single zip codes that are "N/A" or "0"
            if "," not in row['ZipCode(s)']:
                single_zip_code = row['ZipCode(s)']
                if single_zip_code != '0' and single_zip_code != 'N/A':

                    if single_zip_code not in zip_code_count:
                        zip_code_count[single_zip_code]=0
                    zip_code_count[single_zip_code]=zip_code_count[single_zip_code]+1

            #create lists of zip codes when row['ZipCode(s)'] contains multiple zip code values
            if "," in row['ZipCode(s)']:
                zip_code_lists = row['ZipCode(s)'].split(", ")

                #create a counter that adds permits from zip_code_lists to the dictionary
                #and filter out zip codes that are "0"
                for zip_code in zip_code_lists:
                    if zip_code != '0':

                        if zip_code not in zip_code_count:
                            zip_code_count[zip_code]=0
                        zip_code_count[zip_code]=zip_code_count[zip_code]+1

                    
#check that everything has worked correctly by printing the dictionary
pp.pprint(zip_code_count)

#write the dictionary to a csv file for Tableau visualization

with open('zip_code_count.csv', 'w') as newcsvfile:
    header = ['Zip Code', 'Count']
    writer = csv.writer(newcsvfile)
    writer.writerow(header)
    for key, value in zip_code_count.items():
        writer.writerow([key, value])
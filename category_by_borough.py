import pandas as pd

#create a smaller csv file, limited to relevant columns and EventTypes
df = pd.read_csv('Film_Permits.csv', usecols=['EventID','EventType', 'StartDateTime', 'Borough','Category','ZipCode(s)'])
df = df[df['EventType'] != 'Rigging Permit']
df = df[df['EventType'] != 'Theater Load in and Load Outs']
df.to_csv('Smaller_Film_Permits.csv', index=False)

#count instances of each category by borough
myfile = pd.read_csv("Smaller_Film_Permits.csv")
category_by_borough = myfile.groupby(['Borough','Category'],as_index=False).EventID.count()

#check that everything has worked correctly by printing the dataframe
print(category_by_borough)

#write the dataframe to a csv file for visualizing in Tableau
category_by_borough.to_csv('category_by_borough.csv', header=['Borough', 'Category', 'Count of Permits'], encoding='utf-8', index=False)
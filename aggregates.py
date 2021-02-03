# Author:  
# Date: 1/30/21 
# Purpose:Produce a "acquistions_facts" file with the schema that holds the aggregates stats.
# Save it as a CSV file with a header to the working directory.
# Aggregates are calculated at year level

#importing pandas package
import pandas as pd

#import datetime library
import datetime

import os
import dateutil

#Assigning the input dataset files

p = 'people.csv'

#defining the output dataset file
print("Defining aggregates Data Set...");
fileO = open("acquistion_facts.csv", "w+")

#opening three input files
#read the people.csv file, only the required column is extracted.
cols = ["created_dt"]

#Parse the date column in date format. 
in_p = pd.read_csv(p, parse_dates = cols, usecols=cols)

#Extracting the year from the date and storing in a new column
in_p['acquisition_date'] = pd.DatetimeIndex(in_p['created_dt']).year

#print Data Set Details
print('people.csv Data Set Opened')
count_rows = len(in_p.index)
count_cols = len(in_p.columns)
print("No of rows " , count_rows);
print("No of cols " , count_cols);

#Begin Processing
print('Processing Begins....')

#Group By Clause based on year
Frame = in_p.groupby(['acquisition_date']).count()

df_final = Frame.rename(columns={'created_dt':'acquisitions'})

#Writing to the csv from the data frame
df_final.to_csv("acquistion_facts.csv")

print('Processing Completes...')
#End Processing

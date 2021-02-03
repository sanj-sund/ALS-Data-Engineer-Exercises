# Author:  
# Date: 1/30/21 
# Purpose:Produce a "people" file with the follwing schema.
# Save it as a CSV file with a header to the working directory. 

#importing pandas package
import pandas as pd

#import datetime library
import datetime
import os

#Assigning the input dataset files
cons = 'cons.csv'
cons_email = 'cons_email.csv'
cons_email_sub = 'cons_email_chapter_subscription.csv'

##################
print("*******Initial DATA SET details******")
#opening three input files
#read the cons.csv file
in_cons = pd.read_csv(cons)
print('cons.csv Data Set Opened')
count_rows = len(in_cons.index)
count_cols = len(in_cons.columns)
print("No of rows in cons.csv Data Set " , count_rows);
print("No of cols in cons.csv Data Set " , count_cols);

#read the cons_email.csv file
in_cons_email = pd.read_csv(cons_email)
print('cons_email.csv Data Set Opened')
count_rows = len(in_cons_email.index)
count_cols = len(in_cons_email.columns)
print("No of rows in cons.csv Data Set " , count_rows);
print("No of cols in cons.csv Data Set " , count_cols);

#read the cons_email_chapter_subscription.csv file
in_cons_email_s = pd.read_csv(cons_email_sub)
print('cons_email_chapter_subscription.csv Data Set Opened')
count_rows = len(in_cons_email_s.index)
count_cols= len(in_cons_email_s.columns)
print("No of rows in cons_email_chapter_subscription.csv Data Set " , count_rows);
print("No of cols in cons_email_chapter_subscription.csv Data Set " , count_cols);
###################

#defining the output dataset file
fileO = open("people.csv", "w+")
Frame = pd.DataFrame(columns =['email', 'code', 'is_unsub','created_dt','updated_dt'])
Frame.to_csv("people.csv", sep =',')

#Date and Time when the code is executing
print("\n");
ct = datetime.datetime.now()
print('Current date and time = ', ct)

#opening three input files
#read the cons.csv file
col = ['cons_id','source', 'create_dt']
in_cons = pd.read_csv(cons, usecols=col)
print('cons.csv Data Set Opened')
count_rows = len(in_cons.index)
count_cols = len(in_cons.columns)
print("No of rows " , count_rows);
print("No of cols " , count_cols);

#read the cons_email.csv file to extract primary email addresses
cols = ['cons_email_id', 'cons_id', 'is_primary', 'email']
in_cons_email = pd.read_csv(cons_email, usecols=cols)
in_cons_email_p = in_cons_email[in_cons_email.is_primary == 1]
print('cons_email.csv with primary email address Data Set Opened')
count_rows = len(in_cons_email_p.index)
count_cols = len(in_cons_email_p.columns)
print("No of rows " , count_rows);
print("No of cols " , count_cols);

#read the cons_email_chapter_subscription.csv file and extract only with chapter_id = 1
colsc = ['cons_email_id', 'chapter_id', 'isunsub']
in_cons_email_s = pd.read_csv(cons_email_sub, usecols=colsc)
in_cons_email_sc = in_cons_email_s[in_cons_email_s.chapter_id == 1]
print('cons_email_chapter_subscription.csv wit chapter_id = 1 Data Set Opened')
count_rows = len(in_cons_email_sc.index)
count_cols= len(in_cons_email_sc.columns)
print("No of rows " , count_rows);
print("No of cols " , count_cols);

#Begin Processing
print("\nProcessing Begins")
print("Merge the Data Set cons_email and cons_email_chapter_subscription on cons_email_id");

#merging cons_email and cons_email_chapter_subscription data set as email address is the main
#driver and is part of cons_email data set
#A left join is used as we need all primary email addresses
df = pd.merge(in_cons_email_p, in_cons_email_sc, on='cons_email_id', how='left');
#Merging with cons data set to extract source and create_dt
df_final = pd.merge(df, in_cons, on='cons_id', how='left');

count_rows = len(df_final.index)
count_cols = len(df_final.columns)
print("No of rows " , count_rows);
print("No of cols " , count_cols);

cols = df_final.columns.values.tolist()
print("Final Data Set contains columns: \n", cols)

ct = datetime.datetime.now();
ct = ct.__str__();  

#Copying to a dataframe only the columns that were needed for the output dataset
df_final = df_final.rename(columns={'source':'code', 'isunsub':'is_unsub', 'create_dt': 'created_dt'})

#Copying the required data into a dataframe.
Frame = df_final[['email','code','is_unsub','created_dt']].copy()
#Updating with todays date
Frame['updated_dt'] = ct

#Writing it to a CSV file
Frame.to_csv("people.csv")
#Frame.close()
print("\n Processing Completed");







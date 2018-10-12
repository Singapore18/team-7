import pandas as pd
import csv
import math

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

response_file = "responses_180815.csv"
response_df = pd.read_csv(response_file)
# all column names
column_names = list(response_df.columns.values)
l = len(column_names)
# skip the first and last 4 nonsense
for i in range(1, l - 4):
	mres = column_names[i]
	mres = mres.replace("<strong>","")
	mres = mres.replace("</strong>","")
	if i == l - 5:
		print("(\"{}\")".format(mres))
	else:
		print("(\"{}\"),".format(mres))
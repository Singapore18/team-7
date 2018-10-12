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
#print(response_df[column_names[1]][0])
l = len(column_names)
column_names_formatted = []
for i in range(l):
	mres = column_names[i]
	mres = mres.replace("<strong>","")
	mres = mres.replace("</strong>","")
	column_names_formatted.append(mres)
tab = "    "
print('{')
print(tab + '"survey_responses": [')
offset = 7
for i in range(8,l-4):
	prequel = tab + tab + str(i - offset) + ': ["'
	data1 = column_names_formatted[i] + '"' + ', '
	data2 = str(response_df[column_names[i]][0])
	postquel = "],"
	if is_number(data2):
		if math.isnan(float(data2)):
			# delete question
			offset = offset + 1
		else:
			print(prequel + data1 + data2 + postquel)
	else:
		print(prequel + data1 + '"' + data2 + '"' + postquel)
print(tab + "],")
print('}')
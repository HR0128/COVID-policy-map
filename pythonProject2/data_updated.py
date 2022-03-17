import pymssql
import csv

conn = pymssql.connect(server='chronon.som.yale.edu', user='coviddata_sr2364', password='tRhw4u]tHIL.z,$H1BF$a7vY', database='COVID19Restrictions')

cursor = conn.cursor()
cursor.execute('SELECT * FROM View_Data_Export')

with open("COVIDDataPull.csv", "w") as file:
    for i in cursor:
        csv.writer(file).writerow(i)

conn.close()

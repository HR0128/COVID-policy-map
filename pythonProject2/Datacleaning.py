import pandas as pd

readerRaw=pd.read_csv("COVIDDataPull.csv", encoding="cp1252", names=["FIPSState", "StateName", "FIPSCounty", "CountyName",
                "CategoryName","PolicyName","StartDate","StartDate_URL",
                'DateEntered',"DateLastUpdated","LastUpdatedBy"]
                      , converters={"FIPSCounty": '{:0>5}'.format})

readerRaw['FIPSCounty'].astype(str)

readerRaw.drop(columns=["FIPSState", "StateName",'LastUpdatedBy','StartDate_URL','DateEntered',"DateLastUpdated"],inplace=True)

#for r in readerRaw["FIPSCounty"]:
 #   r=str(r).zfill(5)

readerRaw.to_csv("cleaned_COVIDDataPull.csv",index=False)
import pandas as pd

#This line reads the csv file, keeping 5 digits
reader=pd.read_csv("Emergency_integrated.csv")

#Convert policy to index
policyname=reader["PolicyName"].astype(str)
policyindex=[]
for i in policyname:
    if "Start" in i:
        policyindex.append(1)
    else:
        policyindex.append(-1)

#This line appends the week start date column
Startweek=sorted(list(set(reader["Startweek"])))
reader["Policyindex"]=policyindex

dict_key = list(zip(reader.Startweek,reader.FIPSCounty))

reader = reader.iloc[: , 1:]
reader = reader.drop(columns=['CountyName', 'CategoryName','PolicyName','StartDate'])
#reader.to_csv("emergency_policyasnumber.csv")
reader_county=pd.to_numeric(reader.FIPSCounty)

#This line reads the county column
county=reader["FIPSCounty"]
county=sorted(list(set(county)))



# Generate a 'difference' dataframe
reader_fips=pd.read_csv("US_FIPS_Codes.csv")#
allcounty=reader_fips['FIPS']
allcounty=sorted(list(set(allcounty)))
allcounty=pd.to_numeric(allcounty)

l=Startweek

try1=sorted(list(set(reader.Startweek)))
#try1=try1.insert(0,"GeoID")
Diffform=pd.DataFrame(index=allcounty, columns=try1)

for col in Diffform.columns:
    Diffform[col].values[:] = 0

for i in dict_key:
    Diffform.loc[i[1],i[0]]=reader[(reader['Startweek']==i[0])&(reader['FIPSCounty']==i[1])].Policyindex.iloc[0]

# Deal with the state-wise orders
for i in allcounty:
    m = int(i // 1000)
    if m in county:
        Diffform.loc[i] = Diffform.loc[i] + Diffform.loc[m]

for i in range(100):
    if i in allcounty:
        Diffform = Diffform.drop(index=i)

Diffform[Diffform>0]=1
Diffform[Diffform<0]=-1
#Diffform.to_csv("emergency_diffform.csv")

#Finally, generate the sum form
Sumform=Diffform

for j in range(len(Sumform.index)):
    for i in range(1,len(Sumform.columns)):
        Sumform.loc[Sumform.index[j],Sumform.columns[i]]=Diffform.loc[Diffform.index[j],Diffform.columns[i]]+Diffform.loc[Diffform.index[j],Diffform.columns[i-1]]
        if Sumform.loc[Sumform.index[j],Sumform.columns[i]]>0:
            Sumform.loc[Sumform.index[j], Sumform.columns[i]]=1
        else:
            Sumform.loc[Sumform.index[j], Sumform.columns[i]] = 0

new_col = Sumform.index
Sumform.insert(loc=0, column='GeoID', value=new_col)

l.insert(0,"GeoID")
Sumform.columns=l

Sumform.to_csv("emergency_sumform.csv")


import pandas as pd

#This line reads the csv file, keeping 5 digits
reader=pd.read_csv("Recreation_park_integrated.csv")

#Convert policy to index
policyname=reader["PolicyName"].astype(str)
recreation_dict={'State or County Beach Closed':0,
                 'Local Park or Beach Closed':1,'National Park or Beach Closed':1,
                 'Local Park or Beach Reopen':-1, 'State or County Beach Reopen':-1,
                  'National Park or Beach Reopen':-1,'State or County Park Closed':1,'State or County Park Reopen':-1}
policyindex=[]
for i in policyname:
        policyindex.append(recreation_dict[i])

#This line appends the week start date column
Startweek=sorted(list(set(reader["Startweek"])))
reader["Policyindex"]=policyindex
dict_key = list(zip(reader.Startweek,reader.FIPSCounty))

reader = reader.iloc[: , 1:]
reader = reader.drop(columns=['CountyName', 'CategoryName','PolicyName','StartDate'])
#reader.to_csv("Recreation_Park_policyasindex.csv")
reader_county=pd.to_numeric(reader.FIPSCounty)

#This line reads the county column
county=reader["FIPSCounty"]#.astype(str)
county=sorted(list(set(county)))

# Generate a 'difference' dataframe
reader_fips=pd.read_csv("US_FIPS_Codes.csv")#
allcounty=reader_fips['FIPS']
allcounty=sorted(list(set(allcounty)))
allcounty=pd.to_numeric(allcounty)

l=Startweek

Diffform=pd.DataFrame(index=allcounty, columns=Startweek)

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

#Diffform.to_csv("recreation_Park_diffform.csv")

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

Sumform.to_csv("recreation_Park_sumform.csv")

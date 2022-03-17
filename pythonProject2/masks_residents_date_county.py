import pandas as pd

#This line reads the csv file, keeping 5 digits
reader=pd.read_csv("mask_residents_integrated.csv")


#Convert policy to index
policyname=reader["PolicyName"].astype(str)
masks_re_dict={'Resident None':-10, 'Resident Mandatory Indoors':2,
              'Resident Recommended':1, 'Resident Mandatory Indoor and Out':3}

policyindex=[]
for i in policyname:
        policyindex.append(masks_re_dict[i])

#This line appends the week start date column
Startweek=sorted(list(set(reader["Startweek"])))
reader["Policyindex"]=policyindex
dict_key = list(zip(reader.Startweek,reader.FIPSCounty))

reader = reader.iloc[: , 1:]
reader = reader.drop(columns=['CountyName', 'CategoryName','PolicyName','StartDate'])
#reader.to_csv("mask_residents_policyasindex.csv")
reader_county=pd.to_numeric(reader.FIPSCounty)

#This line reads the county column
county=reader["FIPSCounty"]#.astype(str)
county=sorted(list(set(county)))

reader_fips=pd.read_csv("US_FIPS_Codes.csv")#
allcounty=reader_fips['FIPS']
allcounty=sorted(list(set(allcounty)))
allcounty=pd.to_numeric(allcounty)

l=sorted(list(set(Startweek)))

Diffform=pd.DataFrame(index=allcounty, columns=sorted(list(set(reader.Startweek))))

for col in Diffform.columns:
    Diffform[col].values[:] = 0

for i in dict_key:
    Diffform.loc[i[1],i[0]]=reader[(reader['Startweek']==i[0])&(reader['FIPSCounty']==int(i[1]))].Policyindex.iloc[0]


# Deal with the state-wise orders
for i in range(len(Diffform.index)):
    m = int(Diffform.index[i] // 1000)
    if m in county:
        for j in range(len(Diffform.columns)):
            if Diffform.loc[m, Diffform.columns[j]]!=0:
                Diffform.loc[Diffform.index[i], Diffform.columns[j]]=Diffform.loc[m, Diffform.columns[j]]


for i in range(100):
    if i in allcounty:
        Diffform = Diffform.drop(index=i)

#Diffform.to_csv("mask_residents_diffform.csv")

#Finally, generate the sum form
Sumform=Diffform

for j in range(len(Sumform.index)):
    for i in range(1,len(Sumform.columns)):
        if Sumform.loc[Sumform.index[j],Sumform.columns[i]]!=Diffform.loc[Diffform.index[j],Diffform.columns[i-1]] and Sumform.loc[Sumform.index[j],Sumform.columns[i]]==0:
            Sumform.loc[Sumform.index[j], Sumform.columns[i]] = Diffform.loc[
                Diffform.index[j], Diffform.columns[i - 1]]
        elif Sumform.loc[Sumform.index[j],Sumform.columns[i]]<0:
            Sumform.loc[Sumform.index[j], Sumform.columns[i]]=0

#for j in range(len(Sumform.index)):
 #   for i in range(1,len(Sumform.columns)):
  #     if Sumform.loc[Sumform.index[j],Sumform.columns[i]]>0:
    #        Sumform.loc[Sumform.index[j], Sumform.columns[i]]=1
     #   else:
      #      Sumform.loc[Sumform.index[j], Sumform.columns[i]] = 0

new_col = Sumform.index
Sumform.insert(loc=0, column='GeoID', value=new_col)

l.insert(0,"GeoID")
Sumform.columns=l

Sumform.to_csv("mask_residents_sumform.csv")

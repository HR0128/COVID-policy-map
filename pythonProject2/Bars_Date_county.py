import pandas as pd

#This line reads the csv file, keeping 5 digits
reader=pd.read_csv("Bars_integrated.csv")


#Convert policy to index
policyname=reader["PolicyName"].astype(str)
bars_dict={"Closed":5, "Capacity 25":4, "Capacity 50":3, "Capacity 50plus":2,
 "Capacity 100":-10, "Outdoor":1,"Vaccine Required For Entry - Start":0}

policyindex=[]
for i in policyname:
        policyindex.append(bars_dict[i])

#This line appends the week start date column
Startweek=sorted(list(set(reader["Startweek"])))
reader["Policyindex"]=policyindex
dict_key = list(zip(reader.Startweek,reader.FIPSCounty))

reader = reader.iloc[: , 1:]
reader = reader.drop(columns=['CountyName', 'CategoryName','PolicyName','StartDate'])
#reader.to_csv("Bars_policyasindex.csv")
reader_county=pd.to_numeric(reader.FIPSCounty)

#This line reads the county column
county=reader["FIPSCounty"]#.astype(str)
county=sorted(list(set(county)))

reader_fips=pd.read_csv("US_FIPS_Codes.csv")#
allcounty=reader_fips['FIPS']
allcounty=sorted(list(set(allcounty)))
allcounty=pd.to_numeric(allcounty)
allcounty=sorted(list(set(allcounty)))


l=Startweek

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
#Diffform.to_csv("Bars_diffform.csv")
#Finally, generate the sum form
Sumform=Diffform

for j in range(len(Sumform.index)):
    for i in range(1,len(Sumform.columns)):
        if Sumform.loc[Sumform.index[j],Sumform.columns[i]]!=Diffform.loc[Diffform.index[j],Diffform.columns[i-1]] and Sumform.loc[Sumform.index[j],Sumform.columns[i]]==0:
            Sumform.loc[Sumform.index[j], Sumform.columns[i]] = Diffform.loc[
                Diffform.index[j], Diffform.columns[i - 1]]
        Sumform.loc[Sumform.index[j], Sumform.columns[i]] = max(0, Sumform.loc[Sumform.index[j], Sumform.columns[i]])

#for i in range(1,len(Sumform.columns)):
 #    if Sumform.loc[32025,Sumform.columns[i]]!=Diffform.loc[32025,Diffform.columns[i-1]] and Sumform.loc[32025,Sumform.columns[i]]==0:
  #       Sumform.loc[32025, Sumform.columns[i]] = Diffform.loc[32025, Diffform.columns[i - 1]]


new_col = Sumform.index
Sumform.insert(loc=0, column='GeoID', value=new_col)

l.insert(0,"GeoID")
Sumform.columns=l

m=['99999']
n=['99998']
o=['99997']
p=['99996']
q=['99995']
h=['99994']

for i in range(1, len(Sumform.columns)):
    m.append(0)
    n.append(1)
    o.append(2)
    p.append(3)
    q.append(4)
    h.append(5)

Sumform.loc[len(Sumform)] =m
Sumform.loc[len(Sumform)] =n
Sumform.loc[len(Sumform)] =o
Sumform.loc[len(Sumform)] =p
Sumform.loc[len(Sumform)] =q
Sumform.loc[len(Sumform)] =h

Sumform.to_csv("Bars_sumform.csv")



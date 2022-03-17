import pandas as pd


#This line reads the csv file, keeping 5 digits
reader=pd.read_csv("Retail_integrated.csv")


#datelist = pd.date_range(date[0], date[-1],freq="7D").tolist()
#date_list=[d.strftime('%Y-%m-%d') for d in datelist]
#print(date_list)

#def intersection(lst1, lst2):
#    lst3 = [value for value in lst1 if value in lst2]
#    return lst3
#print(intersection(date_list, date))



#Convert policy to index
policyname=reader["PolicyName"].astype(str)
retail_dict={"Closed":4, "Capacity 25":3, "Capacity 50":2, "Capacity 50plus":1,
 "Capacity 100":-10, "Vaccine Required For Entry - Start":0}

policyindex=[]
for i in policyname:
        policyindex.append(retail_dict[i])

#This line appends the week start date column
Startweek=sorted(list(set(reader["Startweek"])))
reader["Policyindex"]=policyindex
#reader["Key point"] = reader["Startweek"].astype(str) +','+reader["FIPSCounty"].astype(str)
#reader["Weekly change"] = reader["FIPSCounty"].astype(str) +','+reader["Policyindex"].astype(str)

#print(dict_key)
dict_key = list(zip(reader.Startweek,reader.FIPSCounty))

reader = reader.iloc[: , 1:]
reader = reader.drop(columns=['CountyName', 'CategoryName','PolicyName','StartDate'])
#reader.to_csv("Retail_policyasindex.csv")
reader_county=pd.to_numeric(reader.FIPSCounty)

#This line converts the format
#reader_out = reader.set_index(['FIPSCounty',reader.groupby(['FIPSCounty']).cumcount()+1]).unstack().sort_index(level=1, axis=1)
#reader_out.columns = reader_out.columns.map('{0[0]}_{0[1]}'.format)
#reader_out.reset_index()


#reader_out=reader_out.assign(TF)
#print (reader_out)
#for i in county:
    #i=int(i)

#df=pd.DataFrame(index=date,columns=datelist)
#for i in da
#df.loc[df['c1'] == 'Value', 'c2'] = 10
#for i in county:
 #   startdate = reader['StartDate'][(reader["FIPSCounty" == i]) & (reader["PolicyName" == "Stay at Home Start"])]
  #  print(startdate)

#for i in county:
 #   for j in date:
  #      startdate=pd.to_datetime(reader['StartDate'][(reader["FIPSCounty"==i])&(reader["PolicyName"=="Stay at Home Start"])])
   #     enddate=pd.to_datetime(reader['StartDate'][(reader["FIPSCounty"==i])&(reader["PolicyName"=="Stay at Home End"])])
    #    if j>=startdate and j<= enddate:
     #       df[i][j]=1
      #  else:
       #     df[i][j]=0


#print(df)

#df.to_csv("Stayhome_Date_county.csv")
#reader_out.to_csv("test.csv")
#for i in reader:
 #   if i["PolicyName"].str.contains("End"):

# Generate a 'difference' dataframe


#This line reads the county column
county=reader["FIPSCounty"]#.astype(str)
#print(county)
county=sorted(list(set(county)))




reader_fips=pd.read_csv("US_FIPS_Codes.csv")#
allcounty=reader_fips['FIPS']
allcounty=sorted(list(set(allcounty)))
allcounty=pd.to_numeric(allcounty)

l=Startweek

Diffform=pd.DataFrame(index=allcounty, columns=sorted(list(set(reader.Startweek))))
#print(allcounty)
#Diffform=pd.DataFrame(index=county, columns=sorted(list(set(reader.Startweek))))
for col in Diffform.columns:
    Diffform[col].values[:] = 0
#Diffform.at[dict_key[0][1],dict_key[0][0]]=1
#print(Diffform.at[dict_key[0][1],dict_key[0][0]])
#print(dict_key[0][1])
#print(dict_key[0][0])
#print(reader.loc[(reader['Startweek']==dict_key[0][0])&(reader['FIPSCounty']==dict_key[0][1])]['Policyindex'])
#Diffform.at[dict_key[0][1],dict_key[0][0]]=reader.loc[(reader['Startweek']==dict_key[0][0])&(reader['FIPSCounty']==dict_key[0][1])]['Policyindex']
for i in dict_key:
    Diffform.loc[i[1],i[0]]=reader[(reader['Startweek']==i[0])&(reader['FIPSCounty']==int(i[1]))].Policyindex.iloc[0]

#print(Diffform.loc[6001,'2020-5-17'])
#print(reader[(reader['Startweek']=='2020-5-17')&(reader['FIPSCounty']==6001)].Policyindex.iloc[0])

# Deal with the state-wise orders
for i in range(len(Diffform.index)):
    m = int(Diffform.index[i] // 1000)
    if m in county:
        for j in range(len(Diffform.columns)):
            if Diffform.loc[m, Diffform.columns[j]]!=0:
                Diffform.loc[Diffform.index[i], Diffform.columns[j]]=Diffform.loc[m, Diffform.columns[j]]
      #      else:
       #         Diffform.loc[Diffform.index[i], Diffform.columns[j]]=min(Diffform.loc[Diffform.index[i], Diffform.columns[j]], Diffform.loc[Diffform.index[m], Diffform.columns[j]])

#print(Diffform.loc[6001,'2020-5-17'])
#print(reader[(reader['Startweek']=='2020-5-17')&(reader['FIPSCounty']==6001)].Policyindex.iloc[0])

for i in range(100):
    if i in allcounty:
        Diffform = Diffform.drop(index=i)

#Diffform = Diffform.drop(index=11)
#Diffform=Diffform.drop(index=lambda x: x in county and x < 100)

#Diffform[Diffform>0]=1
#Diffform[Diffform<0]=-1
#Diffform = Diffform[~(Diffform == 0).any(axis=1)]
#Diffform.to_csv("Retail_diffform.csv")

#Finally, generate the sum form
Sumform=Diffform

for j in range(len(Sumform.index)):
    for i in range(1,len(Sumform.columns)):
        if Sumform.loc[Sumform.index[j],Sumform.columns[i]]!=Diffform.loc[Diffform.index[j],Diffform.columns[i-1]] and Sumform.loc[Sumform.index[j],Sumform.columns[i]]==0:
            Sumform.loc[Sumform.index[j], Sumform.columns[i]] = Diffform.loc[
                Diffform.index[j], Diffform.columns[i - 1]]
        Sumform.loc[Sumform.index[j], Sumform.columns[i]] = max(0, Sumform.loc[Sumform.index[j], Sumform.columns[i]])

        #if Sumform.loc[Sumform.index[j],Sumform.columns[i]]>0:
        #    Sumform.loc[Sumform.index[j], Sumform.columns[i]]=1
       # else:
         #   Sumform.loc[Sumform.index[j], Sumform.columns[i]] = 0
  #  Sumform[Sumform.columns[i]]=pd.to_numeric(Sumform[Sumform.columns[i]])
#Sumform[Sumform>0]=1
#Sumform[Sumform<0]=0
#Sumform= Sumform[~(Sumform == 0).any(axis=1)]

new_col = Sumform.index
Sumform.insert(loc=0, column='GeoID', value=new_col)

l.insert(0,"GeoID")
Sumform.columns=l

Sumform.to_csv("Retail_sumform.csv")

#for col in list(set(Startweek)):
 #   for row in county:
  #      m=col.astype(str)+','+row.astype(str)
   #     print(m)
    #    if m in dict:
     #       Diffform.at[row, col]=reader['Policyindex',reader.loc['Key point'==m]]
      #  else:
       #     Diffform.at[row, col] =0
#Diffform.to_csv("diffform.csv")


# Then we generate the weekstart date list, as column name
# We use the fipscounty as index

# Actually, for each date, generate a vector (FIPSCounty, weekly change)
# Use a dictionary???
# Weekly change by default is 0, unless
# Each date adds up the weekly change


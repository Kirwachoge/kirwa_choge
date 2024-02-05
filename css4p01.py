# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""
cleaning the data
"""
import pandas as pd
df = pd.read_csv("movie_dataset.csv")
#pd.set_option('display.max_rows',None)
#df.drop(['Rank'],inplace=True,axis=1)
x = df["Revenue (Millions)"].mean()

df["Revenue (Millions)"].fillna(x, inplace = True)
x = df["Metascore"].mean()

df["Metascore"].fillna(x, inplace = True)

"""
average revenue
"""
# df[df['Rating']==df['Rating'].max()]
# print (df)  
# print(df[['Rating']][df.Rating == df.Rating.max()])
# print(df.loc[[54]])
#df['Rating'].mean()
total_revenue = df['Revenue (Millions)'].sum()
numb=df.shape[0]
print(numb)
average=total_revenue/numb
print(average)
#print(df.sum())
#print(sum)
"""
average revenue for 2016
"""
import pandas as pd
df = pd.read_csv("movie_dataset.csv")
#pd.set_option('display.max_rows',None)
#df.drop(['Rank'],inplace=True,axis=1)
x = df["Revenue (Millions)"].mean()

df["Revenue (Millions)"].fillna(x, inplace = True)
x = df["Metascore"].mean()

df["Metascore"].fillna(x, inplace = True)
grouped = df.groupby('Year')
average_2015=grouped['2017'].mean()
print(average_2015)

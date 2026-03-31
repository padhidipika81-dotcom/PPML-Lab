'''write a pandas program to merge two dataframes on a single coulmn'''
import pandas as pd

df1=pd.DataFrame({'ID':[1,2,3],
                  'Name':['John','Alice','Bob']})
df2=pd.DataFrame({'ID':[2,3,4],
                  'Age':[25,30,35]})
merged_df=pd.merge(df1,df2,on='ID',how='right')

#output result
print(merged_df)
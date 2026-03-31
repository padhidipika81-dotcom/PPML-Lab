'''write a pandas program to split the following dataframe into groups basedon school code.
Also check the type of GroupBy object.'''

import pandas as pd
pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
data ={
    'School Code':['s01','s02','s01','s02','s01'],
    'Student Name':['John','Alice','Bob','Eve','Charlie'],
    'Score':[85, 90, 78, 92, 88],
    'index':[0,1,2,3,4]
}
df=pd.DataFrame(data)
print(df)
#group by school code
result=student_groups=df.groupby('School Code')
for name,group in result:
    print("\nGroup: ")
    print(name)
    print(group)
print("\nType of GroupBy object: ")
print(type(result))
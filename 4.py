#convert series to categorical and display category codes
import pandas as pd
s=pd.Series(['apple','banana','orange'])
print(s)
cat_s=s.astype('category')
print(cat_s.cat.codes)
# convert numeric strings with commas to floats
import pandas as pd

s = pd.Series(['1,000', '2,500', '3,750'])
float_s = s.str.replace(',', '').astype(float)

print(float_s)
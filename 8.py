#write a panadas program to create a DataFrame from a dictionary and then transpose it,ensuring that data types remain consistent
import pandas as pd
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print(df.dtypes)
df_t = df.T
df_t = df_t.astype(int)
print("\nTransposed DataFrame:")
print(df_t)
print(df_t.dtypes)
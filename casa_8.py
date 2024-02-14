import pandas as pd

df = pd.read_csv('big-mac-full-index.csv')

# iterrows method

for i,r in df.iterrows():
    print(r['name'], r['local_price'])


# apply method

print(df.apply(lambda row: row['local_price'], axis =1))

import pandas as pd
print(pd.__version__)

df = pd.read_csv('https://raw.githubusercontent.com/ageron/handson-ml2/'
                 'master/datasets/housing/housing.csv')
#print(df)
#print(df.columns)
#df_sorted = df.sort_values(by='median_house_value', ascending=False)
#print(df_sorted)
new_df = df.dropna()
print(new_df.columns)
#print(new_df)
new_sorted = new_df.sort_values(by='median_house_value', ascending=False)
print(new_sorted)
'''
First make sure to run 'pip install -r requirements.txt'
Docs for Pandas module: https://pandas.pydata.org/docs/
'''
import pandas as pd

df = pd.read_csv('data.csv')

print(df.to_string())

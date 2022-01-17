import pandas as pd
import csv

df=pd.read_csv("brown_dwarfs.csv")
print(df.shape)

del df["Luminosity"]

print(df.shape)
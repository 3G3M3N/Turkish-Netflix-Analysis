import numpy as np
import pandas as pd

df = pd.read_csv("netflix_titles.csv")
df

movies = turks.loc[(df["type"]=="Movie")]
movies.shape

category = turks["listed_in"].value_counts()
category
sum(category)

director = turks["director"].value_counts()
director

total = sum(director)
105-total 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

#%%
data = pd.read_csv("C:/Users/e_bab/Documents/4geeks/python-hello/logistic-regression-project-tutorial/bank-marketing-campaign-data.csv", sep = ";")
# print(data.head())
print(data.info())
print(data.shape)

#%%
print(data.duplicated().sum())
print(data[data.duplicated])
print(data.columns.duplicated().sum())
print(data.isnull().sum())


"""
Seaborn: plotting graphs
"""
print("Get data from Iris.csv file")
print("-"*20)
# --------------

import pandas as pd

iris_data_df = pd.read_csv("Iris.csv")
print(iris_data_df.head(5))

print("#"*40, end="\n\n")
################################

print("plotting lineplot: Example-1")
print("-"*20)
# --------------

import matplotlib.pyplot as plt
import seaborn as sns

sns.lineplot(iris_data_df)
plt.show()

print("#"*40, end="\n\n")
################################

print("plotting lineplot: Example-2")
print("-"*20)
# --------------

import matplotlib.pyplot as plt
import seaborn as sns

sns.lineplot(data=iris_data_df, x='Species', y='SepalLengthCm')
plt.show()

print("#"*40, end="\n\n")
################################

print("plotting violinplot: Example-1")
print("-"*20)
# --------------

import matplotlib.pyplot as plt
import seaborn as sns

sns.violinplot(data=iris_data_df, x='Species', y='SepalLengthCm')
plt.show()

print("#"*40, end="\n\n")
################################

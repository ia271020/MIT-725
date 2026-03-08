import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("population.csv")

data = data.dropna()
data = data.drop_duplicates()

data.columns = data.columns.str.replace(" ", "_")

print(data.head())

data['Population'].hist()
plt.show()

top10 = data.head(10)

plt.pie(top10['Population'], labels=top10['Country'], autopct='%1.1f%%')
plt.show()

data.to_csv("clean_population_data.csv", index=False)
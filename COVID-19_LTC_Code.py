import matplotlib.pyplot as plt
import pandas as pd

# Reads csv data into pandas dataframe
df = pd.read_csv('COVID-19_LTC_Data.csv')

# Replaces '<5' values with 4
df = df.replace('<5', 4)

# Counts number of homes counts of each ownership type
home_counts = df['Home Type'].value_counts()

# Converts values in the 'Resident Deaths' column from strings to integers
df['Resident Deaths'] = df['Resident Deaths'].astype(str).astype(int)

# Changes name of home type from 'For-profit (financialized)' to simply 'Financialized'
df = df.replace('For-profit (financialized)', 'Financialized')

# Sums up total deaths and total beds by home type, then calculates proportion of deaths per bed
df2 = df.groupby('Home Type')['Resident Deaths'].sum()
df3 = df.groupby('Home Type')['Beds'].sum()
df4 = df2/df3

# Creates bar plot
df4.plot(kind='bar', fontsize=10, rot=0)
plt.ylim(top=0.07)
plt.title('Proportion of Ontario COVID-19 Deaths/Bed by Home Type')
plt.show()

# Converts values in the '% Residents Over 85 (2018-2019)' column from strings to floats
df['% Residents Over 85 (2018-2019)'] = df['% Residents Over 85 (2018-2019)'].astype(str).astype(float)

# Drops homes for which age data was unavailable
df.dropna()

# Calculates average percentage of residents over 85 by home type
df5 = df.groupby('Home Type')['% Residents Over 85 (2018-2019)'].mean()

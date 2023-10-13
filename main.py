import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

import seaborn as sns

df = pd.read_csv('Pathogen detection Salmonella enterica.csv')

# Descriptive summary of the loaded data
summary = df.describe()
# print(summary)

# Number of missing values per column available
missing_values = df.isnull().sum()
# print(missing_values)

# Separate the missing values rows from the whole data

# missing rows
missing_rows = df.isnull().any(axis=1)
missing_data = df[missing_rows]

# non-missing rows
n_missing_rows = ~df.isnull().any(axis=1)
n_missing_data = df[n_missing_rows]
len(n_missing_data)
n_missing_data.describe()

# Check for missing values of the cleaned dataset
(n_missing_data.isnull().sum())

# Check for duplicated rows in the cleaned dataset
duplicate_rows = n_missing_data[n_missing_data.duplicated()]

# Summary of the clean data
n_missing_data.info()

# Exploring the dataset

# Top 10 most common locations
top_locations = n_missing_data['Location'].value_counts().head(10)
# print(top_locations)

# Most common isolation sources across other variables
top_isolation_sources = n_missing_data['Isolation source'].value_counts().head(10)

#
# The distribution of "Create date" over time (e.g., by year or month)?

D_date = pd.to_datetime(n_missing_data['Create date'], format='%Y-%m-%dT%H:%M:%SZ')
D_dateY = D_date.dt.strftime('%d/%m/%Y').value_counts().sort_index()
# D_dateY = D_date.dt.year
D_dateM = D_date.dt.month
"D-Date is:"

# Group the data by year and count the number of entries in each year
yearly_counts = D_dateY.value_counts().sort_index()

# Ensuring there are no temporal trends or patterns by performing timeseries analysis

# Assuming D_date is my Series with a non-datetime index
D_date = pd.Series([1, 2, 3, 4], index=['2022-01-01', '2022-02-01', '2022-03-01', '2022-04-01'])
# Convert the index to a DateTime-like index
D_date.index = pd.to_datetime(D_date.index)
# Now you have a DateTime-like index, and you can resample the data
monthly_data = D_date.resample('M').count()

# Correlation analysis between the "Min-same" and "Min-diff" columns
correlation_matrix = n_missing_data[['Min-same', 'Min-diff']].corr()
"Correlation Matrix:"

# Number of isolates present in each Serovar group
serovar_count = n_missing_data['Serovar'].value_counts()
"Isolate Counts by Serovar:"

# AMR Genotypes - most prevalent AMR Genotypes and how common they are
AMR_genotypes = n_missing_data['AMR genotypes'].value_counts().head(10)
"Most Prevalent AMR Genotypes:"

# Computed Type Analysis - Antigen, Serotype
serotype_counts = n_missing_data['Computed types'].value_counts().head(10)
# Antigen Formula Analysis
antigen_formulas = n_missing_data['Computed types'].str.extract(r'antigen_formula=([^,]+)')
antigen_formulas[0].value_counts()
# Extract unique combinations of antigen formulas
unique_antigen_combinations = antigen_formulas[0].unique()
"\nUnique Antigen Formulas:"
# Antigen Variability Analysis - Calculate the number of unique antigen variants
unique_antigens = n_missing_data['Computed types'].str.extractall(r'([a-zA-Z]+)=')  # Extract antigen parts
unique_antigens = unique_antigens[0].unique()
antigen_count = len(unique_antigens)
f"Number of Unique Antigens = {antigen_count}"
# Extract the Serotype Part (excluding antigen formulas)
serotype_part = n_missing_data['Computed types'].str.extract(r'serotype=([^,]+)')
Serotype_Counts = serotype_part[0].value_counts()
"\nSerotype Distribution Analysis:"

# Data Integrity Check
# Check for duplicates
duplicate_rows = n_missing_data[n_missing_data.duplicated()]
# Data Profiling
summary_stats = n_missing_data.describe()
print(summary_stats)
import pandas as pd


vac = pd.read_csv('vacation.csv')


print(vac.head())

# Data Cleaning

missing_values = vac.isnull().sum()
print("Missing values in each column:\n", missing_values)

# Example: Reordering a categorical variable
# Assume Income2 is a categorical variable that needs reordering
vac['Income2'] = pd.Categorical(vac['Income2'], categories=["<30k", "30-60k", "60-90k", "90-120k", ">120k"], ordered=True)

# Descriptive Analysis

summary_stats = vac.describe(include='all')
print("Summary statistics:\n", summary_stats)

# Frequency distribution of a categorical variable
income2_freq = vac['Income2'].value_counts()
print("Frequency distribution of Income2:\n", income2_freq)

# Investigating univariate distributions
import matplotlib.pyplot as plt
import seaborn as sns

#  Distribution of Age
plt.figure(figsize=(10, 6))
sns.histplot(vac['Age'], bins=30, kde=True)
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

#  Bar plot for a categorical variable
plt.figure(figsize=(10, 6))
sns.countplot(x='Income2', data=vac, order=vac['Income2'].cat.categories)
plt.title('Income Distribution')
plt.xlabel('Income Categories')
plt.ylabel('Count')
plt.show()

# Assessing dependency structures between variables
#  Correlation matrix for numerical variables
corr_matrix = vac.corr()
print("Correlation matrix:\n", corr_matrix)

#  Heatmap of the correlation matrix
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix Heatmap')
plt.show()

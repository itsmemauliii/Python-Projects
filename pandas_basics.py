# Importing pandas library
import pandas as pd

# Creating a simple DataFrame
data = {
    'Name': ['M', 'P', 'A', 'D'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(df)

# Basic Operations
# 1. View the first few rows
print("\nFirst two rows:")
print(df.head(2))

# 2. View summary info
print("\nSummary info:")
print(df.info())

# 3. Statistical summary (numeric columns)
print("\nStatistical summary:")
print(df.describe())

# 4. Selecting a column
print("\nSelecting the 'Name' column:")
print(df['Name'])

# 5. Filtering rows
print("\nRows where Age > 30:")
print(df[df['Age'] > 30])

# 6. Adding a new column
df['Salary'] = [70000, 80000, 90000, 100000]
print("\nDataFrame after adding 'Salary' column:")
print(df)

# 7. Grouping data
print("\nAverage age by city:")
print(df.groupby('City')['Age'].mean())

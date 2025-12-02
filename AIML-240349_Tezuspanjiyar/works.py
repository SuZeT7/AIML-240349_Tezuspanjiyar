Python 3.12.3 (v3.12.3:f6650f9ad7, Apr  9 2024, 08:18:47) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import pandas as pd

# ============================================================
# TASK 1: Load the dataset
# ============================================================
print("=" * 60)
print("TASK 1: Loading Dataset")
print("=" * 60)

df = pd.read_csv('bank.csv')
print("Dataset loaded successfully!")
print(f"Shape: {df.shape[0]} rows and {df.shape[1]} columns\n")

# ============================================================
# TASK 2: Check info and identify required details
# ============================================================
print("=" * 60)
print("TASK 2: DataFrame Information")
print("=" * 60)

# Display DataFrame info
print("DataFrame Info:")
df.info()
print("\n")

# (a) Columns with dtypes=object
print("(a) Columns with dtype='object':")
object_columns = df.select_dtypes(include=['object']).columns.tolist()
print(object_columns)
print("\n")

... # (b) Unique values of those columns
... print("(b) Unique values in object columns:")
... for col in object_columns:
...     print(f"{col}: {df[col].unique()}")
... print("\n")
... 
... # (c) Total number of null values in each column
... print("(c) Null values in each column:")
... print(df.isnull().sum())
... print("\n")
... 
... # ============================================================
... # TASK 3: Drop object columns and save to CSV
... # ============================================================
... print("=" * 60)
... print("TASK 3: Dropping Object Columns")
... print("=" * 60)
... 
... # Drop columns with dtype object
... df_numeric = df.drop(columns=object_columns)
... print(f"Columns dropped: {object_columns}")
... print(f"New DataFrame shape: {df_numeric.shape[0]} rows and {df_numeric.shape[1]} columns")
... 
... # Write to CSV
... df_numeric.to_csv('banknumericdata.csv', index=False)
... print("Data saved to 'banknumericdata.csv'\n")
... 
... # ============================================================
... # TASK 4: Read the new CSV and find summary statistics
... # ============================================================
... print("=" * 60)
... print("TASK 4: Summary Statistics")
... print("=" * 60)
... 
... # Read the numeric data CSV
... df_numeric_read = pd.read_csv('banknumericdata.csv')
... print("Read 'banknumericdata.csv' successfully!")
... print("\nSummary Statistics:")

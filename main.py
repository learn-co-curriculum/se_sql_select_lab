# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('data.sqlite')

# STEP 1B
# cur = conn.cursor()
employees = pd.read_sql("""
SELECT * FROM employees;
""", conn)

# STEP 2
# Replace None with your code
df_first_five = pd.read_sql("""
SELECT employeeNumber, lastName FROM employees
""", conn)

# STEP 3
# Replace None with your code
df_five_reverse = pd.read_sql("""
SELECT lastName, employeeNumber FROM employees
""", conn)

# STEP 4
# Replace None with your code
df_alias = None

# STEP 5
# Replace None with your code
df_executive = None

# STEP 6
# Replace None with your code
df_name_length = None

# STEP 7
# Replace None with your code
df_short_title = None

# STEP 8
# Replace None with your code
sum_total_price = None

# STEP 9
# Replace None with your code
df_day_month_year = None


print(df_five_reverse)
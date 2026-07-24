# STEP 1A
# Import SQL Library and Pandas
import sqlite3
from pathlib import Path

import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect(Path(__file__).with_name("data.sqlite"))


# Add code below and run file to see data from employees table

employee_data = pd.read_sql("""SELECT * FROM employees""", conn)
print("---------------------Employee Data---------------------")
print(employee_data)
print("-------------------End Employee Data-------------------")


# STEP 2
# employee number and last name for all employees
df_first_five = pd.read_sql("""
SELECT employeeNumber, lastName
FROM employees
""", conn)


# STEP 3
# same as step 2, but lastName comes before employeeNumber
df_five_reverse = pd.read_sql("""
SELECT lastName, employeeNumber
FROM employees
""", conn)


# STEP 4
# same as step 3, but employeeNumber is aliased as ID
df_alias = pd.read_sql("""
SELECT lastName, employeeNumber AS ID
FROM employees
""", conn)


# STEP 5
# bin jobTitle into 'Executive' vs 'Not Executive' using CASE
df_executive = pd.read_sql("""
SELECT
    CASE
        WHEN jobTitle = 'President' OR jobTitle = 'VP Sales' OR jobTitle = 'VP Marketing'
        THEN 'Executive'
        ELSE 'Not Executive'
    END AS role
FROM employees
""", conn)


# STEP 6
# length of each employee's last name
df_name_length = pd.read_sql("""
SELECT LENGTH(lastName) AS name_length
FROM employees
""", conn)


# STEP 7
# first two letters of each person's job title
df_short_title = pd.read_sql("""
SELECT SUBSTR(jobTitle, 1, 2) AS short_title
FROM employees
""", conn)


# Add the code below and run the file to see order details data

order_details = pd.read_sql("""SELECT * FROM orderDetails;""", conn)
print("------------------Order Details Data------------------")
print(order_details)
print("----------------End Order Details Data----------------")


# STEP 8
# sum of the rounded (priceEach * quantityOrdered) across all orders
sum_total_price = pd.read_sql("""
SELECT ROUND(priceEach * quantityOrdered) AS total_price
FROM orderDetails
""", conn).sum().to_numpy()


# STEP 9
# original order date plus day/month/year broken out into their own columns
df_day_month_year = pd.read_sql("""
SELECT
    orderDate,
    STRFTIME('%d', orderDate) AS day,
    STRFTIME('%m', orderDate) AS month,
    STRFTIME('%Y', orderDate) AS year
FROM orders
""", conn)


if __name__ == "__main__":
    print("\n--- df_first_five ---")
    print(df_first_five)

    print("\n--- df_five_reverse ---")
    print(df_five_reverse)

    print("\n--- df_alias ---")
    print(df_alias)

    print("\n--- df_executive ---")
    print(df_executive)

    print("\n--- df_name_length ---")
    print(df_name_length)

    print("\n--- df_short_title ---")
    print(df_short_title)

    print("\n--- sum_total_price ---")
    print(sum_total_price)

    print("\n--- df_day_month_year ---")
    print(df_day_month_year)

# Close the connection
conn.close()

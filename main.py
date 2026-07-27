import sqlite3
import pandas as pd

# STEP 1A & 1B: Connect to the database
conn = sqlite3.connect("data.sqlite")

# Reference code provided by lab:
employee_data = pd.read_sql("""SELECT * FROM employees""", conn)


# STEP 2: Select employee number and last name
df_first_five = pd.read_sql(
    """SELECT employeeNumber, lastName FROM employees""", conn
)


# STEP 3: Last name before employee number
df_five_reverse = pd.read_sql(
    """SELECT lastName, employeeNumber FROM employees""", conn
)


# STEP 4: Alias employee number as 'ID'
df_alias = pd.read_sql(
    """SELECT lastName, employeeNumber AS ID FROM employees""", conn
)


# STEP 5: CASE statement for executive roles
df_executive = pd.read_sql(
    """
    SELECT *,
           CASE 
               WHEN jobTitle IN ('President', 'VP Sales', 'VP Marketing') THEN 'Executive'
               ELSE 'Not Executive'
           END AS role
    FROM employees
""",
    conn,
)


# STEP 6: Length of last name as 'name_length'
df_name_length = pd.read_sql(
    """SELECT LENGTH(lastName) AS name_length FROM employees""", conn
)


# STEP 7: First two letters of job title as 'short_title'
df_short_title = pd.read_sql(
    """SELECT SUBSTR(jobTitle, 1, 2) AS short_title FROM employees""", conn
)

# Reference code provided by lab:
order_details = pd.read_sql("""SELECT * FROM orderDetails;""", conn)


# STEP 8: Total amount for all orders (summed inside SQL and extracted cleanly)
sum_total_price = pd.read_sql(
    """
    SELECT SUM(ROUND(priceEach * quantityOrdered)) AS total_price 
    FROM orderDetails
""",
    conn,
)["total_price"]


# STEP 9: Extract Day, Month, Year from orderDate
df_day_month_year = pd.read_sql(
    """
    SELECT orderDate,
           strftime('%d', orderDate) AS day,
           strftime('%m', orderDate) AS month,
           strftime('%Y', orderDate) AS year
    FROM orders
""",
    conn,
)


# Close the connection
conn.close()
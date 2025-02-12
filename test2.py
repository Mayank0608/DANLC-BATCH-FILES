#Lab2: Write a Pandas program to drop the rows where at least one element is
#missing in a given DataFrame.

import pandas as pd

# Creating the DataFrame
df = pd.DataFrame({
    'ord_no': [70001, None, 70002, 70004, None, 70005, None, 70010, 70003, 70012, None, 70013],
    'purch_amt': [150.5, 270.65, 65.26, 110.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6],
    'ord_date': ['2012-10-05', '2012-09-10', None, '2012-08-17', '2012-09-10', '2012-07-27',
                 '2012-09-10', '2012-10-10', '2012-10-10', '2012-06-27', '2012-08-17', '2012-04-25'],
    'customer_id': [3002, 3001, 3001, 3003, 3002, 3001, 3001, 3004, 3003, 3002, 3001, 3001],
    'salesman_id': [5002, 5003, 5001, None, 5002, 5001, 5001, None, 5003, 5002, 5003, None]
})

# Dropping rows with at least one missing value
df_cleaned = df.dropna()

# Display the cleaned DataFrame
print("DataFrame after dropping rows with missing values:")
print(df_cleaned)

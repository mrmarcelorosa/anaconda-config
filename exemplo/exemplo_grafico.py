import pandas as pd
import matplotlib.pyplot as plt

excel_file = 'exemplo/sales_example.xlsx'

df = pd.read_excel(excel_file)

monthly_revenue = df.groupby('Date')['Revenue'].sum()

plt.figure()
monthly_revenue.plot(kind='bar')
plt.title('Monthly Revenue 2025')
plt.ylabel('Revenue (USD)')
plt.xlabel('Month')
plt.tight_layout()
plt.show()

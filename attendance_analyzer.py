
# Student Attendance Analyzer - Python Script Version

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load sample data
df = pd.read_csv('sample_data.csv', parse_dates=['Date'])

# Preprocessing
df['Month'] = df['Date'].dt.to_period('M').astype(str)
df['Present'] = df['Status'].apply(lambda x: 1 if x == 'Present' else 0)

# Monthly Attendance by Class
monthly_attendance = df.groupby(['Class', 'Month']).agg(
    Total=('Present', 'count'),
    Present=('Present', 'sum')
).reset_index()
monthly_attendance['Attendance_Percentage'] = (monthly_attendance['Present'] / monthly_attendance['Total']) * 100

# Print Summary
print("Monthly Attendance Rates by Class:")
print(monthly_attendance[['Class', 'Month', 'Attendance_Percentage']])

# Plot Bar Chart
plt.figure(figsize=(8, 6))
sns.barplot(data=monthly_attendance, x='Class', y='Attendance_Percentage', hue='Month')
plt.axhline(90, color='red', linestyle='--', label='90% Threshold')
plt.title('Monthly Attendance by Class')
plt.ylim(0, 100)
plt.legend()
plt.tight_layout()
plt.show()

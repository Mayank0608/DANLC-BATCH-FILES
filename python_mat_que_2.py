import matplotlib.pyplot as plt

# Given data
income_sources = ['Salary', 'Freelance', 'Investments', 'Rental', 'Other']
monthly_income = [5000, 1500, 1000, 600, 400]

# Create pie chart
plt.figure(figsize=(7, 7))
plt.pie(monthly_income, labels=income_sources, autopct='%1.1f%%',
        colors=['blue', 'green', 'red', 'purple', 'orange'], startangle=140)
plt.title("Monthly Income Distribution")
plt.show()

# Conclusion
print("The pie chart shows that Salary is the major source of income, contributing the highest percentage.")
print("Freelance work and investments contribute significantly, while rental and other sources form a smaller portion.")

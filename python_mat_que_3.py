import matplotlib.pyplot as plt

# Given data
segments = ['Product A', 'Product B', 'Services', 'Licensing']
revenue_percentages = [45, 25, 15, 15]

# Create pie chart
plt.figure(figsize=(7, 7))
plt.pie(revenue_percentages, labels=segments, autopct='%1.1f%%',
        colors=['blue', 'green', 'red', 'purple'], startangle=140)
plt.title("Company Revenue Distribution")
plt.show()

# Conclusion
print("The pie chart shows that Product A is the major revenue generator, contributing 45% of total revenue.")
print("Product B follows with 25%, while Services and Licensing each contribute 15%.")
print("This distribution highlights the company's dependency on Product A and B for the majority of its revenue.")

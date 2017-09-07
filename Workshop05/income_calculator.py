incomes = []
months = int(input("How many months? "))
for month in range(1, months + 1):
    income = float(input("Enter income for month " + str(month) + ": "))
    incomes.append(income)
print()
print("Income Report")
print("-------------")
total = 0
for month in range(1, months + 1):
    income = incomes[month - 1]
    total += income
    print("Month", format(month, "2d"), "- Income: $",
          format(income, "10.2f"),
          "Total: $", format(total, "10.2f"))

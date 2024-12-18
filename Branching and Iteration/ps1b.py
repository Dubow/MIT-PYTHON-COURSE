annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, in decimals: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi annual raise, as a decimal: "))
portion_down_payment = 0.25
r = 0.04
current_saving = 0
down_payment = total_cost * portion_down_payment   #getting the value of the money needed for downpayment
month = 0
while current_saving < down_payment:
    monthly_return = current_saving * r/12
    monthly_salary_saved = (annual_salary/12) * portion_saved
    current_saving = current_saving + monthly_salary_saved + monthly_return
    month +=1

    if month % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
print(f"Number of months needed for you to save for down payment is: {month}")

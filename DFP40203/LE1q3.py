# Ask the user for input
car_price = 90000
down_payment = float(input("Please enter your down payment: "))
loan_period_in_years = int(input("How long you want to make a loan in years (1 to 9 years only): "))
interest_rate = 0.027
loan_period_in_months=loan_period_in_years*12


# Calculate the loan amount and monthly payment

loan_amount = car_price - down_payment
total_interest = interest_rate*loan_amount*loan_period_in_years
monthly_payment = (loan_amount+total_interest)/(loan_period_in_months)



if down_payment <= 9000:
    print("You are not eligible")
else:
    print("You need to pay",round(monthly_payment,2)," monthly as your monthly payment")
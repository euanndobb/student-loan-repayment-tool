# Tool to predict whether it is worth paying off your student loan with payments above the existing 9% of what you earn over £27k.


current_salary = 40000

allowance_sl = 31395

boe_base_interest = 4 #If there is good future model for this - apply it (perhaps as an API...)
retail_price_index = 5

loan_rate = min(boe_base_interest, retail_price_index) + 1

# Assuming you get paid monthly - loan repayments are taken from the gross payment (pre-tax)

#pre-tax

repayment = 0.09 * (current_salary - allowance_sl)

net_income = ((current_salary - repayment) - 12500)*(1 - 0.4) + 12500

print(repayment, net_income)

after_tax = (current_salary - 12500)*0.6 + 12500

repayment2 = max((after_tax - allowance_sl)*0.09, 0)

net_income2 = after_tax - repayment

print(repayment2, net_income2)








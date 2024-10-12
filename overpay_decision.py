import numpy as np
import matplotlib.pyplot as plt  

data = {
        'sl_threshold' : 31395,
        'sl_interest_rate' : 0.05,
        'sl_threshold' : 31395,
        'uni_years' : 4,
        'standard_repayment_rate' : 0.09,
        'sl_initial_value' : 50000
}


def repayment_data(av_gross_salary, repayment_rate, data):
    
    sl_threshold = data['sl_threshold']
    sl_interest_rate = data['sl_interest_rate']
    sl_initial_value = data['sl_initial_value']
    uni_years = data['uni_years']
    standard_repayment_rate = data['standard_repayment_rate']

    # Assume (uni_years) years at university, where the installments are staggered with equal value:

    sl_balance_upon_working = 0

    for i in range(uni_years):

        sl_balance_upon_working += (sl_initial_value / uni_years) * (1 + sl_interest_rate) ** (i+1)  

    # The above determines the balance on finishing university.

    sl_lifespan = 30 - uni_years

    # Assume the sl lifespan is less than the working lifespan of the user.

    standard_repayment = max(repayment_rate * (av_gross_salary - sl_threshold), 0)

    full_repayment_year =  sl_lifespan # Assume that some debt will be written off by default. 

    balances = [sl_balance_upon_working]  # For year 0 (item 0) post graduation, this is the balance.


    for i in range(sl_lifespan):

        balance = balances[i] * (1 + sl_interest_rate) - standard_repayment

        if balance > 0:

            balances.append(balance)
        
        else: 

            full_repayment_year = i + 1
            balances.append(0)
            last_repayment = balances[-2] # Always the second last balance - as the last balance is 0. 

            break



    if full_repayment_year == sl_lifespan:  # Case of some final amount being writen off. 

        total_repayment = standard_repayment * sl_lifespan

        years = np.linspace(0, sl_lifespan, sl_lifespan + 1)


    # Need to deal with the full_repayment_year = 1 case

    elif full_repayment_year == 1:

        total_repayment = last_repayment

        years = np.linspace(0, full_repayment_year, full_repayment_year +  1)

    else: # Case of loan being repayed before the expiry timeframe ends. 

        total_repayment = standard_repayment * (full_repayment_year - 1) + last_repayment #change

        years = np.linspace(0, full_repayment_year, full_repayment_year + 1)


    return balances, years, total_repayment



#arguments - current salary; when you first took the loan out, current balance, 
#1 Career projections
#2 Current position:

# Projected_average_salary, what are you willing to overpay by per year?, 


def should_you_overpay(av_gross_salary, willing_to_overpay_per_annum, data):

    standard_repayment_rate = data['standard_repayment_rate']
    sl_threshold = data['sl_threshold']

    excess_repayment_rate_max = willing_to_overpay_per_annum / (av_gross_salary - sl_threshold)

    repayment_rate_max = standard_repayment_rate + excess_repayment_rate_max

    # The optimal rate is obviously to pay it all off at once - but this is a trivial solution...

    total_repayment_noaction = repayment_data(av_gross_salary, standard_repayment_rate, data)[2]

    # Potentially add a function that goes a little further if there is an upcoming cliff..

    total_repayment_action = repayment_data(av_gross_salary, repayment_rate_max, data)[2]

    if total_repayment_noaction > total_repayment_action:

        print(str(salary)+ ': you should overpay to save in the long run: ' + str(total_repayment_noaction - total_repayment_action))

    else:
        print(str(salary) + ': do nothing')

    return 0


salaries = np.arange(0, 200000, 10)


total_repayments = []

for salary in salaries:
    
    balances, years, total_repayment = repayment_data(salary, data['standard_repayment_rate'], data)

    total_repayments.append(total_repayment)
    #plt.plot(years, balances)


# plt.grid()
# plt.show()

plt.plot(salaries, total_repayments)
plt.show()

print(repayment_data(1500000, data['standard_repayment_rate'], data))


salary = 90000
willing_to_overpay = 5000

should_you_overpay(salary, willing_to_overpay, data)

#test
#test
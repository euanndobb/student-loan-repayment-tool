# import numpy as np
# import matplotlib.pyplot as plt
# # Tax thresholds dictionary contains a 2 element list consisting of the maximum salary within the tax band and the rate at which tax is paid within the tax band.

# # this is inclusive of NI

# tax_thresholds = { "personal allowance" : [12571, 0], 
#                   "basic rate" : [50270, 0.20], 
#                   "higher rate" : [125140, 0.40],
#                   "additional rate" : [float('inf'), 0.45]
#                   }

# ni_thresholds = { "personal allowance" : [12571, 0], 
#                   "basic rate" : [50270, 0.08], 
#                   "higher rate" : [125140, 0.02],
#                   }

# # Personal allowance reduced by £1 for every £2 that your adjusted net income is above £100,000.
# # Neglect NI contributions for now...



# gross_salary = 120000
# personal_allowance_threshold = 100000


# def personal_allowance_reduction(gross_salary, personal_allowance_threshold, tax_thresholds):

#     personal_allowance = tax_thresholds['personal allowance'][0]

#     reduction = 0

#     if gross_salary < personal_allowance_threshold:

#         return 0
    
#     elif gross_salary >= personal_allowance_threshold:

#         reduction = (gross_salary - personal_allowance_threshold) / 2

#         return min(reduction, personal_allowance)
    

# def ni_deductions(gross_salary, ni_thresholds):

#     ni_basic_max = (ni_thresholds['basic rate'][0] - ni_thresholds['personal allowance'][0]) * ni_thresholds['basic rate'][1]

#     if gross_salary < ni_thresholds['personal allowance'][0]:

#         ni_deduction = 0
    
#     elif gross_salary < ni_thresholds['basic rate'][0]:

#         ni_deduction = (gross_salary - ni_thresholds['personal allowance'][0]) * ni_thresholds['basic rate'][1]
    
#     else: 
#         ni_deduction = (gross_salary - ni_thresholds['basic rate'][0]) * ni_thresholds['higher rate'][1] + ni_basic_max

#     return ni_deduction
    


# def take_home_income(gross_salary, personal_allowance_threshold, tax_thresholds, ni_thresholds):

#     pa_reduction = personal_allowance_reduction(gross_salary, personal_allowance_threshold, tax_thresholds)

#     ni_ded = ni_deductions(gross_salary, ni_thresholds)

#     total_taxation = 0

#     basic_max = tax_thresholds['basic rate'][1] * (tax_thresholds['basic rate'][0] - tax_thresholds['personal allowance'][0])
#     higher_max = tax_thresholds['higher rate'][1] * (tax_thresholds['higher rate'][0] - tax_thresholds['basic rate'][0])
#     # additional_max = tax_thresholds['additional rate'][1] * (tax_thresholds['additional rate'][0] - tax_thresholds['higher rate'][0])

#     if gross_salary < tax_thresholds['basic rate'][0]:

#         total_taxation += max(tax_thresholds['basic rate'][1] * (gross_salary - tax_thresholds['personal allowance'][0]), 0)
#         # print('tax at 20 %: ' + str(total_taxation))

#     elif gross_salary < tax_thresholds['higher rate'][0]:

#         total_taxation += basic_max
#         total_taxation += tax_thresholds['higher rate'][1] * (gross_salary - tax_thresholds['basic rate'][0])
#         # print('tax at 20 %: ' + str(basic_max))
#         # print('tax at 40 %: ' + str(total_taxation - basic_max))

#     elif gross_salary < tax_thresholds['additional rate'][0]:

#         total_taxation += (basic_max + higher_max)
#         total_taxation += tax_thresholds['additional rate'][1] * (gross_salary - tax_thresholds['higher rate'][0])
#         # print('tax at 20 %: ' + str(basic_max))
#         # print('tax at 40 %: ' + str(higher_max))
#         # print('tax at 45 %: ' + str(total_taxation - basic_max - higher_max))

#     # pa_reduction always taxed at the 'higher' band of tax...

#     take_home_income = gross_salary - total_taxation - tax_thresholds['higher rate'][1] * pa_reduction - ni_ded

#     return take_home_income




# #Plot what is going on here.


# take_home_income1 = take_home_income(170000, personal_allowance_threshold, tax_thresholds, ni_thresholds)

# print(take_home_income1)

# step = 10


# salaries = np.arange(0, 200000, step)


# take_homes = []


# for salary in salaries:
#     take_home = take_home_income(salary, personal_allowance_threshold, tax_thresholds, ni_thresholds)
#     take_homes.append(take_home)



# plt.plot(salaries, take_homes)
# plt.title('Gross Salary vs. Take Home Salary')
# plt.grid()
# plt.xlabel('Gross salary (£)')
# plt.ylabel('Take Home Salary (£)')
# plt.xlim([0, salaries[-1]])
# plt.ylim([0, take_homes[-1]])
# plt.show()


# take_homes = np.array(take_homes)

# rates = np.diff(take_homes)/step

# salaries_for_rates = np.linspace(0, 200000, len(rates))



# plt.plot(salaries_for_rates, rates)
# plt.xlabel('Gross Salary (£)')
# plt.ylabel('Take-home Proportion of Gross Salary (£/£)')
# plt.xlim([0, salaries[-1]])
# plt.grid()
# plt.show()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Tax thresholds dictionary contains a 2-element list consisting of the maximum salary within the tax band and the rate at which tax is paid within the tax band.
tax_thresholds = {
    "personal allowance": [12571, 0],
    "basic rate": [50270, 0.20],
    "higher rate": [125140, 0.40],
    "additional rate": [float('inf'), 0.45]
}

ni_thresholds = {
    "personal allowance": [12571, 0],
    "basic rate": [50270, 0.08],
    "higher rate": [125140, 0.02],
}

personal_allowance_threshold = 100000

def personal_allowance_reduction(gross_salary, personal_allowance_threshold, tax_thresholds):
    personal_allowance = tax_thresholds['personal allowance'][0]
    reduction = 0
    if gross_salary < personal_allowance_threshold:
        return 0
    else:
        reduction = (gross_salary - personal_allowance_threshold) / 2
        return min(reduction, personal_allowance)

def ni_deductions(gross_salary, ni_thresholds):
    ni_basic_max = (ni_thresholds['basic rate'][0] - ni_thresholds['personal allowance'][0]) * ni_thresholds['basic rate'][1]

    if gross_salary < ni_thresholds['personal allowance'][0]:
        ni_deduction = 0
    elif gross_salary < ni_thresholds['basic rate'][0]:
        ni_deduction = (gross_salary - ni_thresholds['personal allowance'][0]) * ni_thresholds['basic rate'][1]
    else:
        ni_deduction = (gross_salary - ni_thresholds['basic rate'][0]) * ni_thresholds['higher rate'][1] + ni_basic_max

    return ni_deduction

def income_tax(gross_salary, personal_allowance_threshold, tax_thresholds):
    pa_reduction = personal_allowance_reduction(gross_salary, personal_allowance_threshold, tax_thresholds)

    total_taxation = 0
    basic_max = tax_thresholds['basic rate'][1] * (tax_thresholds['basic rate'][0] - tax_thresholds['personal allowance'][0])
    higher_max = tax_thresholds['higher rate'][1] * (tax_thresholds['higher rate'][0] - tax_thresholds['basic rate'][0])

    if gross_salary < tax_thresholds['basic rate'][0]:
        total_taxation += max(tax_thresholds['basic rate'][1] * (gross_salary - tax_thresholds['personal allowance'][0]), 0)
    elif gross_salary < tax_thresholds['higher rate'][0]:
        total_taxation += basic_max
        total_taxation += tax_thresholds['higher rate'][1] * (gross_salary - tax_thresholds['basic rate'][0])
    elif gross_salary < tax_thresholds['additional rate'][0]:
        total_taxation += (basic_max + higher_max)
        total_taxation += tax_thresholds['additional rate'][1] * (gross_salary - tax_thresholds['higher rate'][0])

    total_taxation += tax_thresholds['higher rate'][1] * pa_reduction

    return total_taxation

def take_home_income(gross_salary, personal_allowance_threshold, tax_thresholds, ni_thresholds):
    ni_ded = ni_deductions(gross_salary, ni_thresholds)
    tax_ded = income_tax(gross_salary, personal_allowance_threshold, tax_thresholds)
    return gross_salary - ni_ded - tax_ded

# Plotting the breakdown
step = 10
salaries = np.arange(0, 200001, step)

take_homes = []
ni_contributions = []
tax_contributions = []

for salary in salaries:
    ni_ded = ni_deductions(salary, ni_thresholds)
    tax_ded = income_tax(salary, personal_allowance_threshold, tax_thresholds)
    take_home = take_home_income(salary, personal_allowance_threshold, tax_thresholds, ni_thresholds)

    take_homes.append(take_home)
    ni_contributions.append(ni_ded)
    tax_contributions.append(tax_ded)

# Convert lists to numpy arrays for easier calculations
take_homes = np.array(take_homes)
ni_contributions = np.array(ni_contributions)
tax_contributions = np.array(tax_contributions)

# Plotting the stacked area chart
plt.fill_between(salaries, 0, take_homes, label='Take Home Pay', color='g', alpha=0.6)
plt.fill_between(salaries, take_homes, take_homes + ni_contributions, label='NI Contributions', color='b', alpha=0.6)
plt.fill_between(salaries, take_homes + ni_contributions, take_homes + ni_contributions + tax_contributions, label='Tax Contributions', color='r', alpha=0.6)

# Customizing the tick labels
def thousands_formatter(x, pos):
    return f'{int(x / 1000)}k'

# Set the custom formatter for both axes
plt.gca().xaxis.set_major_formatter(FuncFormatter(thousands_formatter))
plt.gca().yaxis.set_major_formatter(FuncFormatter(thousands_formatter))

plt.xlabel('Gross Salary (£)')
plt.ylabel('Amount (£)')
plt.title('Gross Salary Breakdown: Take Home, NI, and Tax Contributions')
plt.legend()
plt.grid(True)
plt.xlim([0, 200000])
plt.ylim([0, 200000])
plt.show()
plt.plot()


############################

take_home_rates = np.diff(take_homes) / step

salaries_rates = np.linspace(0, 200000, len(take_home_rates))



def thousands_formatter(x, pos):
    return f'{int(x / 1000)}k'

# Set the custom formatter for both axes
plt.gca().xaxis.set_major_formatter(FuncFormatter(thousands_formatter))



plt.plot(salaries_rates, take_home_rates)
plt.ylabel('Take-home Salary Proportion for Add. Earning (£/£)')
plt.xlabel('Gross Salary (£)')
plt.grid(True)
plt.xlim([0, salaries_rates[-1]])
plt.show()
plt.plot()










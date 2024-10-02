from taxation import take_home_income, ni_deductions, income_tax
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

###########################################################

# Tax thresholds dictionary contains a 2-element list consisting 
# of the maximum salary within the tax band and the rate at which 
# tax is paid within the tax band.

tax_thresholds = {
    "personal allowance": [12571, 0],
    "basic rate": [50270, 0.20],
    "higher rate": [125140, 0.40],
    "additional rate": [float('inf'), 0.45]
}

# Similar setup for the NI.

ni_thresholds = {
    "personal allowance": [12571, 0],
    "basic rate": [50270, 0.08],
    "higher rate": [125140, 0.02],
}

personal_allowance_threshold = 100000

###########################################################


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

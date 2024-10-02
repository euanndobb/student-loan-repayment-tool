from taxation import take_home_income

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

salary = 113000

print(take_home_income(salary, personal_allowance_threshold, tax_thresholds, ni_thresholds))








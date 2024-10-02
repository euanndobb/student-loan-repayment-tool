import numpy as np
import matplotlib.pyplot as plt


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












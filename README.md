## Student Loan Repayment Tool ##

This tool is under development and will be designed to inform the user whether it is favourable to pay back their student loan in a bulk payment, or continue to make repayments at the automatic rate.

Features at present:

- taxation.py contains functions that allow the user the to calculate their takehome salary using the arguments of gross income and information regarding the current income tax and NI contribution brackets.
- plotter.py plots gross salaries between £0 and £200k, visualising the contribution to NI and income tax respectively.
- plotter.py also plots the proportion of take-home salary gained for an increase in gross salary for the same range of gross income. It interestingly shows a c.60% taxation of earnings between 100k and 125k due to the onset of the loss of Personal Allowance.
- main.py simply allows the user to compute their take-home pay. 

Future features:

- Tool to predict future salary based on current salary (this could require a model trained on salary data)
- Tool to model future interest rates (SLC adds 1% the lower of the BoE Base and Retail Index)
- Based on a student loan present value, make a recommendation for a threshold salary at which bulk repayments could be beneficial.

Notes:

- Student Loan is written off after x (30?) years.
- Consider normal working lifespan.
- 



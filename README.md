## Student Loan Repayment Tool ##

This tool is under development and will be designed to inform the user whether it is favourable to overpay on their student loan, or continue to make repayments at the standard rate.

### Features at present: ###

### taxation.py ### 

- contains functions that allow the user the to calculate their takehome salary using the arguments of gross income and information regarding the current income tax and NI contribution brackets.

### plotter.py ###

- plots gross salaries between £0 and £200k, visualising the contribution to NI and income tax respectively.
- plots the proportion of take-home salary gained for an increase in gross salary for the same range of gross income (essentially, this is the taxation rate for additional money earned in this range). It interestingly shows a c.60% taxation of earnings between 100k and 125k due to the onset of the loss of Personal Allowance.

### main.py ### 

- simply allows the user to compute their take-home pay.

### overpay_decision ###

- This function allows the user (who we assume is just starting work) to enter a lifetime mean salary projection and amount which they are willing to overpay annually of the student loan.
- The depending on the credentials the user enters, they will be advised whether to overpay or maintain the standard rate of repayment.
- The function will return what the user stands to save in total repayment (future cash flow is not discounted here).
- The assumption is that the overpayment, if applicable is paid on a monthly basis.

### Future features: ###

- Tool to predict future salary based on current salary (this could require a model trained on salary data)
- Tool to model future interest rates (SLC adds 1% the lower of the BoE Base and Retail Index)
- Based on a student loan present value, make a recommendation for a threshold salary at which bulk repayments could be beneficial.

Notes:

- Student Loan is written off after x (30?) years.
- Consider normal working lifespan.
- test!



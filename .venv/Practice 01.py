#Write some Python code that performs the following tasks:
#Takes in the present value, annual interest rate, and expected future value from the user.

#Calculates the total number of years it would take to reach a given expected future value,
#rounds your answer to the nearest year, and prints it to the screen.

#Prints the future value at the end of each year as shown below.

###
#Enter the amount of funds you would like to invest today in dollars (Present Value, or PV): 1000
#Enter the annual interest rate: 0.1
#Enter the total dollar amount you would like to have in the future (Future Value, or FV): 2000
###

years = 1
amount = 1000
interest_rate = 0.1
fv = 2000

while True:
    amount = amount + (interest_rate * amount)
    print('FV in Year {} = ${}'.format(years, round(amount,1)))
    if amount >= fv:
        print('It would take {} years to reach ${}'.format(years, amount))
        break
    years = years + 1

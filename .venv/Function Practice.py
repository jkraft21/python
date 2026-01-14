#Assume that you have been tasked to develop a Python function that calculates
#the effective annual rate (EAR) of return. EAR considers the effect of compounding
#within the year and can be calculated from the nominal (or stated) annual rate of return (𝑖)
#using the following formula:
EAR = (1 + 𝑖/𝑚)𝑚 – 1,
#where 𝑚 represents the number of compounding periods per year.

#Complete the following tasks:
# a)Define a Python function that calculates the effective annual rate of return.
# The function should receive the nominal (stated) annual rate and
# the number of compounding periods per year.
# b)Assume that you deposited $1,000 today into an account paying 10% compounded quarterly.
# Calculate the effective annual rate of return using the function defined in Task 1.
# Round your answer to four decimal places.
# c)Calculate the amount of interest you would have earned by the end of the year.
# Round your answer to four decimal places.
# d)Repeat Tasks 2 and 3, but with interest compounded monthly.

def Calculate_EAR(i,m):
    return ((1+(𝑖/𝑚))**m)-1

i = float(input('nominal interest rate'))
m = float(input('number of compounding periods'))

#call Function
EAR = Calculate_EAR(i,m)
print('The Effective Annual Interest Rate is {}'.format(round(EAR,4)))

def Calculate_InterestNotional(pv,ear):
    return (pv * ear)

pv = float(input('present value'))
ear = float(EAR)

Int = Calculate_InterestNotional(pv, ear)
print('The Interest Notional Earned is ${}'.format(round(Int,4)))

#This program helps to calculate the value of investment where the interest rate varies year over year.
#
#Author: Seyi Idowu
#        30-Jan-2020
#
#Description: this python program calculates the value of investment
#
#user input values for initial investment principal, and interest rate for year 1

SENTINEL = 0

initial_principal = float(input("Enter the amount you initially invested: "))
interest_rate = float(input("What is the interest rate for year 1: "))
principal = initial_principal
year = 1

# calculate the principal for each year as the user input the interest rate for that year

while (SENTINEL != interest_rate):
    principal = principal * (1 + (interest_rate / 100))
    year = year + 1
    interest_rate = float(input("What is the interest rate for year {:}: ".format(year)))

# code calculate average income from the interest rate, and stop when user input zero for interest rate
# investment worth after the number of years and the average yearly income from interest is printed

try:
    average_income = (principal - initial_principal) / (year - 1)
    print( "At the end of {:} years, your investment will be worth ${:,.2f}".format(year - 1,principal))
    print("Your average yearly income is ${:,.2f}".format(average_income))
except ZeroDivisionError:
    print("Your interest rate cannot be zero")



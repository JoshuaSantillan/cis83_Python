## Name: Joshua Santillan
## Date: 2/19/20
## Description : ask for input for a price and print sales tax and total
##

## set variables for both the state and county tax
statetax = .075
countytax = .025
x = float(input("Enter the amount of the purchase: "))

print(x) 

statecost= x*statetax
countycost = x*countytax
totaltax = round(x*statetax*countytax,2)
totalprice = round(x+countycost+statecost,2)

print("Your item cost:", x)
print("State Tax:", statecost)
print("County Tax:", countycost)
print("Total sales tax:", totaltax)
print("Total Price with tax:",totalprice)
## Name: Joshua Santillan
## Date: 2/18/20
## Email: santillanj125821@student.vvc.edu
## Class: cis83 spr-2020
## Description: if elseif branching practice program.
'''
psuedo-code: 
1% -inf < x < = 50k
2% 50k < x <= 75k
3% 75k < x <= 100k
4% 100k < x <= 250k
5% 250k < x <= 500k
6% x> 500k 
'''
# use this variable to check tax bracket conditions
tax = 50000

if tax <= 50000:
    print("1%")
elif tax > 50000  and tax <= 75000 :
    print("2%")
elif tax > 75000 and tax <= 100000:
    print("3%")
elif tax >100000 and tax <= 250000:
    print("4%")
elif tax >250000 and tax <= 500000:
    print("5%")
else:
    print("6%")

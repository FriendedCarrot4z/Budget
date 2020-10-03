"""
This is program 1/3 this program will do simple budget savings
"""
print("This program will take your income and expenses and tell you how much you have left")
#gets the inputs for your budget
income = float(input('Enter your income: '))
tax = float(input('Enter your tax rate: '))
phone = float(input('Enter your phone bill: '))
food = float(input('Enter your monthly grocery bill: '))
gas = float(input('Enter your monthly gas bill: '))
insher = float(input('Enter your monthly insherance bill: '))
other = float(input('Enter your other monthly expenses: '))
#calualtes how much money you have after each expense
Ntax = (income - (income * tax))
Nphone = (Ntax - phone)
Nfood = (Nphone - food)
Ngas = (Nfood- gas)
Ninsher = (Ngas - insher)
Nother = (Ninsher - other)
tithing = (Nother - (income * 0.1))
Yincome = income * 12

taxBrack = str() #checks the tax braket you're in
if income > 0.0 and Yincome < 15100.0:
    taxBrack = (" 1 which is 10%")
elif Yincome > 15100.0 and Yincome < 61300.0:
    taxBrack = (" 2 which is 15%")
elif Yincome > 61300.0 and Yincome < 123700.0:
    taxBrack = (" 3 which is 20%")
elif Yincome > 123700.0 and Yincome - 123700.0:
     taxBrack = (" 4 which is 28%")
elif Yincome > 188450.0 and Yincome < 336550.0:
     taxBrack = (" 5 which is 33%")
elif Yincome >= 336550.0:
    taxBrack = (" 6 which is 35%")

#prints out how much money you have and the expenses in a table
print('The following is a report on your monthly expenses')
print('Item                  Budget          Actual')
print('=============== =============== ===============')
print('Income', '{:> 40.2f}'.format(income))
print('You are in tax bracket {:>24}'.format(taxBrack))
print('After Taxes', '{:> 35.2f}'.format(Ntax))
print('After Phone', '{:> 35.2f}'.format(Nphone))
print('After Food', '{:> 36.2f}'.format(Nfood))
print('After Gas', '{:> 37.2f}'.format(Ngas))
print('After Inserance', '{:> 31.2f}'.format(Ninsher))
print('After Other', '{:> 35.2f}'.format(Nother))
print('After Tithing ', '{:> 32.2f}'.format(tithing))
if tithing < 0:
    print("You don't have enough money")
else:
    print('remander', '{:> 38.2f}'.format(tithing))

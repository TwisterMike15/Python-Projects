#Python Program 1- Compound Interest
#Michael Gorse, Anthony Carrola, and Brittany Marietta

#Prints out a description of what the program does for user
print('This is a compound interest calculator. Enter the values for the variables')     
print('in the compund interest equation, and this will produce the result for A')
print('(the amount of money in the account ater a specified number of years)\n')

#Reads in data for each variable as a string, then converts it to a float, so it can be manipulated
p = float(input('Enter P. It is the principle amount deposited into the account.')) 
r = float(input('Enter r. This is the anual interest rate. Enter this value as a percentage \n(ie: 2.5 for 2.5% interest)'))
r = r/100
n = float(input('Enter n. This is the number of times per year the interest is compounded.'))
t = float(input('Enter t. This is the number of years.'))

#equation used to calculate a
a = p*(1+(r/n))**(n*t)

print('\nA is', a)

'''
Write a program that calculates the total number of a
meal purchased at a restaurant. The program should ask
the user to enter the charge for the food, and then
calculate the amount of an 18 percent tip and 7 percent
sales tax. Display each of these amounts and the total.
'''

base_charge = float(input('Enter charge for food: '))
tip = base_charge * 0.18
tax = base_charge * 0.07
total = base_charge + tip + tax

print('Base charge:', base_charge)
print('18% Tip:', tip)
print('Tax:', tax)
print('Total, including tip:', total)

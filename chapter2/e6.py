'''
Write a program that will ask the user to enter the
amount of a purchase. The program should then
compute the state and country sales tax. Assume the
state sales tax is 5 percent and the country sales tax
is 2.5 percent. The program should display the amount
of the purchase, the state sales tax, the country sales
tax, and the total of the sale (which is the sum of
the amount of the purchase plus the total sales tax).
'''

purchase_price = float(input('Enter purchase amount: '))

# Calculate
state_tax = purchase_price * 0.05
country_tax = purchase_price * 0.025
total_tax = state_tax + country_tax
total = purchase_price + total_tax

print('Purchase price:', purchase_price)
print('State sales tax:', state_tax)
print('Country sales tax:', country_tax)
print('Total sales tax:', total_tax)
print('Total:', total)

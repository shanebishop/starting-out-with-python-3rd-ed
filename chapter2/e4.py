'''
A customer in a store is purchasing five items. Write a
program that asks for the price of each item, and then
displays the subtotal of the sale, the amount of sales
tax, and the total. Assume the sales tax is 7 percent.
'''

# Get prices
price1 = float(input('Price 1: '))
price2 = float(input('Price 2: '))
price3 = float(input('Price 3: '))
price4 = float(input('Price 4: '))
price5 = float(input('Price 5: '))

# Calculate
subtotal = price1 + price2 + price3 + price4 + price5
sales_tax = subtotal * 0.07
total = subtotal + sales_tax

print('Subtotal:', subtotal)
print('Sales tax:', sales_tax)
print('Total:', total)

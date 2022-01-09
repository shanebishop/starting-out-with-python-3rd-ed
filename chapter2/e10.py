'''
A cookie recipe calls for the following ingredients:
-1.5 cups of sugar
-1 cup of butter
-2.75 cups of flour

The recipe produces 48 cookies with this amount of
ingredients. Write a program that asks the user how
many cookies he or she wants to make, and then
displays the number of cups of each ingredient
neeed for the specified number of cookies.
'''

cookies = int(input('Enter desired number of cookies: '))

ratio = cookies / 48

cups_sugar = 1.5 * ratio
cups_butter = ratio  # 1 * ratio = ratio
cups_flour = 2.75 * ratio

print('Cups of sugar:', cups_sugar)
print('Cups of butter:', cups_butter)
print('Cups of flour:', cups_flour)

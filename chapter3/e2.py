'''
The area of a rectangle is the rectangle's length times
its width. Write a program that asks for the length and
width of two rectangles. The program should tell the
user which rectangle has the greater area, or if the
areas are the same.
'''

width1 = float(input('Enter width 1:'))
len1 = float(input('Enter length 1: '))

width2 = float(input('Enter width 2:'))
len2 = float(input('Enter length 2: '))

area1 = len1 * width1
area2 = len2 * width2

if area1 > area2:
    print('Rectangle 1 has larger area.')
elif area2 > area1:
    print('Rectangle 2 has larger area.')
else:
    print('Rectangles have equal areas.')

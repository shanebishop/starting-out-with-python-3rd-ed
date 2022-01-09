'''
Write a program that asks the user for the number of
males and the number of females registered in a class.
The program should display the percentage of males and
females in the class.
'''

num_males = int(input('Enter number of males:'))
num_females = int(input('Enter number of females:'))

total_students = num_males + num_females

percent_males = num_males / total_students * 100
percent_females = num_females / total_students * 100

print('Percent males: ', percent_males, '%', sep='')
print('Percent_females: ', percent_females, '%', sep='')

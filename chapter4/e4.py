mph = float(input('What is the speed of the vehicle in mph? '))
total_hours = int(input('How many hours has it traveled? '))

# Don't print anything of hours is less than 1
if total_hours < 1:
    exit()

print('Hour\tDistance Traveled')

# stop is total_hours+1 to include total_hours
for hours in range(1, total_hours+1):
    print(hours, mph * hours, sep='\t')

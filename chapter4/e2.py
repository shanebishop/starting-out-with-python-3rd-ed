CAL_PER_MINUTE = 4.2

# 31 is used as stop since 30 should be included
for minutes in range(10, 31, 5):
    burned = minutes * CAL_PER_MINUTE
    print('Calories burned after', minutes, 'minutes:', burned)

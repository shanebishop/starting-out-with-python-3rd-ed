from math import ceil

DOGS_PER_PKG = 10
BUNS_PER_PKG = 8

attendees = int(input('Enter number of attendees: '))
dogs_per_person = int(input('Enter number of hot dogs per person: '))

used_dogs = attendees * dogs_per_person
dog_pkgs = ceil(used_dogs / DOGS_PER_PKG)
bun_pkgs = ceil(used_dogs / BUNS_PER_PKG)
leftover_dogs = dog_pkgs * DOGS_PER_PKG - used_dogs
leftover_buns = bun_pkgs * BUNS_PER_PKG - used_dogs

print('Hot dog packages required:', dog_pkgs)
print('Hot dog bun packages required:', bun_pkgs)
print('Leftover hot dogs:', leftover_dogs)
print('Leftover hot dog buns:', leftover_buns)

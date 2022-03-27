#!/usr/bin/env python
# coding=utf-8
"""
Birthday Paradox Simulation, by Al Sweigart al@inventwithpython.com
Explore the surprising probabilities of the "Birthday Paradox".
More info at https://en.wikipedia.org/wiki/Birthday_problem
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, math, simulation
"""

import datetime, random


def getBirthday(numberOfBirthday):
    """
    Returns a list of number random date objects for birthdays.
    """
    birthdays = []
    for i in range(numberOfBirthday):
        # The year is unimportant for our simulation, as long as all
        # birthdays have the same year.
        startOfYear = datetime.date(2001, 1, 1)

        # Get a random day into the year:
        randomNumberOfDay = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDay
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):
    """
    Returns the date object of a birthday that occurs more than once
    in the birthdays list.
    """
    if len(birthdays) == len(set(birthdays)):
        return None  # All birthdays are unique, so return None.

    # Compare each birthday to every other birthday:
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1:]):
            if birthdayA == birthdayB:
                return birthdayA  # Return the matching birthday.


# Display the intro:
    print('''
          Birthday Paradox, by Al Sweigart al@inventwithpython.com
          The Birthday Paradox shows us that in a group of N people, the odds
          that two of them have matching birthdays is surprisingly large.
          This program does a Monte Carlo simulation (that is, repeated random
          simulations) to explore this concept.
          (It's not actually a paradox, it's just a surprising result.)
          ''')


# Set up a tuple of month names in order:
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jum',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:
    # Keep asking until the user enters a valid amount.
    print('How many birthdays shall I generate?(Max 100)')
    reponse = input('> ')
    if reponse.isdecimal and (0 < int(reponse) <= 100):
        numBDays = int(reponse)
        break
print()


# Generate and display the birthdays:
print('Here are ', numBDays, 'birthdays:')
birthdays = getBirthday(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        # Display a comma for each birthday after the first birthday.
        print(', ', end='')
        monthName = MONTHS[birthday.month - 1]
        dateText = '{} {}'.format(monthName, birthday.day)
        print(dateText, end='')
print()
print()


# Determine if there are two birthdays that match.
match = getMatch(birthdays)

# Display the results:
print('In this simulation, ', end='')
if match != None:
    monthName = MONTHS[match.month - 1]
    dataText = '{} {}'.format(monthName, match.day)
    print('multiple people have a birthday on', dateText)
else:
    print('there are no matching birthdays.')
print()


# Run through 100,000 simulations:
print('Generating', numBDays, 'random birthdays 100,000 times ...')
input('Press Enter to begin...')

print('Let\'s run another 100,000 simulations.')
simMatch = 0
for i in range(100_000):
    if i % 10_000 == 0:
        print(i, 'simulations run...')

    birthdays = getBirthday(numBDays)
    if getMatch(birthdays) != None:
        simMatch += 1
print('100,000 simulations run.')

# Display simulation results:
probability = round(simMatch / 100_000 * 100, 2)
print('Out of 100,000 simulations of', numBDays, 'people, there was a')
print('matching birthday in that group', simMatch, 'times. This means')
print('that', numBDays, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think!')

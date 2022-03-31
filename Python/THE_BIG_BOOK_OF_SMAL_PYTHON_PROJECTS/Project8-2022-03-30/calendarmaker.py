#!/usr/bin/env python
# coding=utf-8
"""
Calendar Maker, by Al Sweigart al@inventwithpython.com
Create monthly calendars, saved to a text file and fit for printing.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short
"""

import datetime

# set up the constants.
DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
        'Saturday')
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December')

print('Calendar Maker, by Al Sweigart al@inventwithpython.com')

while True:
    # Loop to get a year from the user.
    print('Enter the year fot the calendar:')
    reponse = input('> ')

    if reponse.isdecimal() and int(reponse) > 0:
        year = int(reponse)
        break
    print('Please enter a numeric year, like 2023.')
    continue

while True:
    # Loop to get a month from the user.
    print('Enter the month for the calendar,1-12:')
    reponse = input('> ')

    if not reponse.isdecimal():
        print('Please enter a numeric month, like 3 for March.')
        continue

    month = int(reponse)
    if 1 <= month <= 12:
        break


def getCalendarFor(year, month):
    calText = ''  # calText will contain the string of our calendar.

    # put the month and year at the top of the calendar.
    calText += (' ' * 34) + MONTHS[month - 1] + ' ' + str(year) + '\n'

    # add the days of the week labels to the calendar.
    # (!) try changing this to abbreviations: SUN, MON, TUE, etc.
    calText = '...Sunday.....Monday....Tuesday...Wednesday...Thursday....\
Friday....Saturday..\n'

    # the horizontal line string that separate weeks.
    weekSeparator = ('+----------' * 7) + '+\n'

    # the blank rows have ten spaces in between the | day separators.
    blankRow = ('|          ' * 7) + '|\n'

    # get the first date in the month. (The datetime module handles all
    # the complicated calendar stuff for us here.)
    currentDate = datetime.date(year, month, 1)

    # Roll back currentDate until it is Sunday. ( weekday() returns 6
    # for Sunday, not 0.)
    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days=1)

    while True:
        # loop over each week in the month.
        calText += weekSeparator

        # dayNumberRow is the row with the day number labels.
        dayNumberRow = ''
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += '|' + dayNumberLabel + (' ' * 8)
            currentDate += datetime.timedelta(days=1)  # go to next day
        dayNumberRow += '|\n'  # add the vertical line after Saturday.

        # add the day number row and 3 blank rows to the calendar text.
        calText += dayNumberRow
        for i in range(3):
            # (!) try changing the 4 to a 5 or 10.
            calText += blankRow

        # check if we're done with the month.
        if currentDate.month != month:
            break

    # add the horizontal line at the very bottom of the calendar.
    calText += weekSeparator
    return calText


calText = getCalendarFor(year, month)
print(calText)  # display the calendar

# save the calendar to a text file.
calendarFilename = 'calendar_{}_{}.txt'.format(year, month)
with open(calendarFilename, 'w') as fileObj:
    fileObj.write(calText)

print('Save to ' + calendarFilename)

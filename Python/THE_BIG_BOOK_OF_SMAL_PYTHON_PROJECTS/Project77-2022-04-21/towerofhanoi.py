#!/usr/bin/env python
# coding=utf-8
"""
The Tower of Hanoi, by Al Sweigart al@inventwithpython.com
A stack-moving puzzle game.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, game, puzzle
"""

import copy
import sys

TOTAL_DISKS = 5
# start with all disks on tower A.
COMPLETE_TOWER = list(range(TOTAL_DISKS, 0, -1))


def main():
    print("""
          The Tower of Hanoi, by Al Sweigart al@inventwithpython.com

          Move the tower of disks, one disk at a time, to another tower. Larger
          disks cannot rest on top of a smaller disk.

          More info at https://en.wikipedia.org/wiki/Tower_of_Hanoi
          """)

    # set up the towers, the end of the list is the top of the tower
    towers = {'A': copy.copy(COMPLETE_TOWER), 'B': [], 'C': []}

    while True:
        # display the towers and disks
        displayTowers(towers)

        # ask the user for a move
        fromTower, toTower = askForPlayerMove(towers)

        # move the top disk from fromTower to toTower.
        disk = towers[fromTower].pop()
        towers[toTower].append(disk)

        # check if the user has solved the puzzle.
        if COMPLETE_TOWER in (towers['B'], towers['C']):
            displayTowers(towers)
            print('You have solved the puzzle! Well done!')
            sys.exit()


def askForPlayerMove(towers):
    """ask the player for a move. returns (fromTower, toTower)."""

    while True:
        print('Enter the letters of "from" and "to" towers, or QUIT.')
        print('(e.g. AB to moves a disk from tower A to tower B.)')
        response = input('> ').upper().strip()

        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        # make sure the user entered valid tower letters.
        if response not in ('AB', 'AC', 'BA', 'BC', 'CA', 'CB'):
            print('Enter one of AB, AC, BA, BC, CA, or CB.')
            continue

        # syntactic sugar - User more descrptive variable names.
        fromTower, toTower = response[0], response[1]

        if len(towers[fromTower]) == 0:
            # the "from" tower cannot be an empty tower.
            print('You selected a tower with no disks.')
            continue
        elif len(towers[toTower]) == 0:
            # any disk can be moved onto an empty "to" tower.
            return fromTower, toTower
        elif towers[toTower][-1] < towers[fromTower][-1]:
            print('Can\'t put larger disks on top og smaller ones.')
            continue
        else:
            # this is a valid move, so return the selected towers
            return fromTower, toTower


def displayTowers(towers):
    """display the current state."""

    # display the three towers.
    for level in range(TOTAL_DISKS, -1, -1):
        for tower in (towers['A'], towers['B'], towers['C']):
            if level >= len(tower):
                displayDisk(0)
            else:
                displayDisk(tower[level])
        print()

    # display the tower labels A, B, and C
    emptySpace = ' ' * (TOTAL_DISKS)
    print('{0} A{0}{0} B{0}{0} C\n'.format(emptySpace))


def displayDisk(width):
    """display a disk of the given width. a width of 0 means no disk."""
    emptySpace = ' ' * (TOTAL_DISKS - width)

    if width == 0:
        # display a pole segment without a disk.
        print(emptySpace + '||' + emptySpace, end='')
    else:
        # display the disk
        disk = '@' * width
        numLabel = str(width).rjust(2, '_')
        print(emptySpace + disk + numLabel + disk + emptySpace, end='')


# if the program is run (instead of imported), run the game
if __name__ == '__main__':
    main()

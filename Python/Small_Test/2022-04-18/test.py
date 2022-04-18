#!/usr/bin/env python
# coding=utf-8
import time
import os
import random
import string

passwordScore = 0


def optionOne():
    global passwordScore
    # Code for checking a password
    os.system('cls')
    print('Option One has been selected')
    password = input('Please type in your password here: ')

    # Password check begins
    if (len(password) > 7) and (password.isspace() is False):
        # Check for capitalisation
        for p in password:
            if p.isupper() is True:
                passwordScore += 1
            else:
                pass

        passwordScore += 2
        for s in string.punctuation:
            # Beginning test for special letters
            for p in password:
                if s == p:
                    passwordScore += 1
                else:
                    pass
    else:
        pass

    # Returning results to the user
    if passwordScore >= 5:
        print('Your password is safe enough to use')
        time.sleep(2)
    elif passwordScore == 3:
        print('We believe your password could be safer')
        time.sleep(2)
    else:
        print('Your password is not safe enough to use')
        print('using this password may place your data at risk')
        time.sleep(2)


def optionTwo():
    # Code for creating a password at random
    print('Option Two has been selected')
    chars = string.ascii_uppercase + string.ascii_lowercase +\
        string.digits + string.punctuation
    size = random.randint(8, 12)
    newPassword = ''.join(random.choice(chars) for x in range(size))
    print(newPassword)


def start():
    print('Option 1: Check my passsword')
    print('Option 2: Create a password')
    option = input('Please chose your option here [ENTER]: ')

    if option == '1':
        # Option 1 has been selected
        return optionOne()
    elif option == '2':
        # Option 2 has been selected
        return optionTwo()
    else:
        # An error has occured
        print('You have not selected a valid option')
        time.sleep(1)
        os.system('cls')
        return start()


for i in range(1):
    start()

# !/usr/bin/env python3
# Created by: Angel
# Created on:March,18 2025
# This program asks the user to
# guess a number between 0 and 9.

import constants


def main():
    # write the guessed number
    number_guessed = int(input("Enter the number guessed: "))
    print("")

    # check if the number guessed is wrong
    if number_guessed > constants.CORRECT_ANSWER:
        print("You guessed wrong!")

    # check if number is wrong
    if number_guessed < constants.CORRECT_ANSWER:
        print("You guessed wrong!")
    # check if number is correct
    if number_guessed == constants.CORRECT_ANSWER:
        print("You guessed correctly!")


if __name__ == "__main__":
    main()

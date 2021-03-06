#! /usr/bin/env python3
# importing the random module
import random

"""
PROGRAMMER: Aiden Peace 
DATE: 7/6/2022
TITLE: Exercise 9 : Guessing Game One
DESCRIPTION: Write a program that takes a list of numbers 
(for example, a = [5, 10, 15, 20, 25]) and makes a new 
list of only the first and last elements of the given list. 
For practice, write this code inside a function.
"""


def main():

    # generating a random number for future usage
    random_number = random.randrange(1, 10)

    # taking in users guess for future usage
    print("Welcome to Aiden's Guessing Random Number Game\nPlease enter 'exit' when you are ready to exit")
    users_guess = input("Enter a number from 1-9: ")
    total_guess = 0

    while users_guess.lower != 'exit':
        if users_guess == 'exit':
            print("You guessed " + str(total_guess) + " times overall Goodbye")
            break
        if int(random_number) == int(users_guess):
            # if the user and the randomly generated number do match
            # we will let the user know they are correct and ask them
            # to play again until they enter 'exit'
            print("You guessed the number correctly!")
            print("Random number was: " + str(random_number))
            print("your number was: " + str(users_guess))
            print()
            total_guess += 1
            random_number = random.randrange(1, 10)
            users_guess = input("Enter a number from 1-9: ")
        else:
            # if the user and the randomly generated number do not match
            # we will tell the user if their guess was too high or too low
            # and ask them to guess again until their guess and
            # random_number are equivalent
            if int(users_guess) < int(random_number):
                print("Your guess was too low. Try again")
            elif int(users_guess) > int(random_number):
                print("Your guess was too high. Try again")
            users_guess = input("Enter a number from 1-9: ")


if __name__ == "__main__":
    main()

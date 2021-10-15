"""
Hang Man Project Python

Author: Braden Franklin
Date: 10/13/21
Course: Intro to computer Programming 1, Tri 1 2021

Description: A terminal hang man style game.

"""
import turtle
import secrets
import math
import tkinter as tk
from os import system
import time

def clearOuput():
    _ = system('cls')

def getWord():

    # Establish List of words based on difficulty

    # Easy
    wordsListEasy = [
        "limit",
        "guest",
        "floor",
        "frank",
        "quest",
        "liver",
        "trail",
        "style",
        "dairy",
        "suite",
        "attic",
        "mouse"
    ]
    # Normal
    wordsListNormal = [
        "excitement",
        "fastidious",
        "repetition",
        "innovation",
        "unpleasant",
        "brainstorm",
        "experiment",
        "restaurant",
        "conference",
        "temptation",
        "houseplant",
        "reluctance"
    ]
    # Hard
    wordsListHard = [
        "investigation",
        "entertainment",
        "consciousness",
        "supplementary",
        "constellation",
        "environmental",
        "comprehensive",
        "preoccupation",
        "recommendation",
        "constitutional",
        "inappropriate",
        "characteristic"
    ]
    # Insane
    wordsListInsane = [
        "supercalifragilisticexpialidocious", 
        "pseudopseudohypoparathyroidism", 
        "floccinaucinihilipilification", 
        "pneumonoultramicroscopicsilicovolcanoconiosis ",
        "antidisestablishmentarianism",
        "thyroparathyroidectomized"
        ]
    # -----------------------------

    # Ask the player to specifiy their desired difficulty and then return a random word based on the difficulty
    while True:
        difficultyChoice = input("Pick your desired difficulty[easy, normal, hard, or insane]:")
        if difficultyChoice == "easy":
            return secrets.choice(wordsListEasy)
        elif difficultyChoice == "normal":
            return secrets.choice(wordsListNormal)
        elif difficultyChoice == "hard":
            return secrets.choice(wordsListHard)
        elif difficultyChoice == "insane":
            return secrets.choice(wordsListInsane)
        else:
            print("Invalid Difficulty chosen, please retry")

def startGame():
    while True:
        wrongAnswersLeft = 6
        word = getWord()
        letters = []
        for i in range(len(word)):
            letters.append(word[i])
        filledSpaces = []
        for i in range(len(word)):
            filledSpaces.append(False)
        print(filledSpaces)
        print(letters)
        print("_ " * len(word))

        while True:
            if wrongAnswersLeft <= 0:
                print("Game over!")
                break
            guess = input("Enter your guess: ")
            time.sleep(1)
            print(guess in letters)
            if not guess in letters:
                wrongAnswersLeft -= 1
                print("That letter is not in the word!, you have" + str(wrongAnswersLeft) + "answers you can get wrong left.")
            if guess.isalpha() and len(guess) == 1:
                new = ""
                for i in range(len(word)):
                    if filledSpaces[i]:
                        new = new + letters[i] + " "
                    else:
                        if guess == letters[i]:
                            new = new + guess + " "
                            filledSpaces[i] = True
                        else:
                            new = new + "_ "

                completed = True
                filledValues = all(i == filledSpaces[0] for i in filledSpaces)
                print(filledValues)
                if filledValues == False:
                    completed = False
                if completed:
                    print("You guessed to word!")
                    print(word)
                    break
                print(new)
            else:
                print("Your guess must be a singular alpha character")
        playAgain = input("Would you like to play again?")
        if playAgain == "yes" or "Yes":
            print("Restarting Game")
            clearOuput()
        else:
            clearOuput()
            break
            
startGame()

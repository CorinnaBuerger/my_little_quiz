# Name: My Little Quiz
# From: Corinna Bürger

from sys import exit

# Greeting
print("Hello to my little quiz! Tell me your name!")
name = input()
print("All right, ", name,". Are you ready? (y/n)")
answer = input()
if answer == "n":
    print("This is your problem. I will ask you anyway.")
if answer == "y":
    print("I didn't expect anything else. Let's start!")

# First Question
print("Question 1: What's the best operating system?")
answer_correct_1 = "Linux"
answer_given_1 = input()
counter = 0
if (answer_given_1 == answer_correct_1):
    print("That's correct! You are smart.")
    counter = counter + 1
else:
    print("That's not correct. The correct answer is 'Linux'")
if (answer_given_1 == "Windows"):
    print("You are stupid. I won't talk to you ever again. Bye.")
    exit(1)

# Second Question
print("Question 2: What is the best programming language?")
answer_correct_2 = "Python"
answer_given_2 = input()
if (answer_given_2 == answer_correct_2):
    print("Correct, again! You are really smart.")
    counter = counter + 1
else:
    print("That's not correct. The correct answer is 'Python'.")

# Third Question
print("Okay, let's do the third and last one: What's the name of the Linux mascot?")
answer_correct_3 = "Tux"
answer_given_3 = input()
if (answer_given_3 == answer_correct_3):
    print("Congratulations! You are great, mate.")
    counter = counter + 1
else:
    print("That's not correct. The correct answer is 'Tux'.")

# Score
if counter == 0:
    print("You scored", counter, ". You are not very smart, are you?")
if counter == 1:
    print("You scored", counter, ". You must be new to this computer stuff.")
if counter == 2:
    print("You scored", counter, ". That's pretty good. Keep going!")
if counter == 3:
    print("You scored ", counter, "points. Are you the god of computer?")
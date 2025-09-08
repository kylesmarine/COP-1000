# PROGRAMMER: RICHARD KYLE MCDONALD
# PROGRAM NAME: COP 1000 – Assignment #01
# DATE WRITTEN: 09/08/2025
# FILENAME: mcdonald_richard_Assign01.py
# PROGRAM PURPOSE: PROMPT THE USER TO INPUT THEIR NAME, COLLEGE MAJOR AND A PYTHON BASED CONCEPT OF INTEREST
# PROGRAM PURPOSE: DISPLAY THE RESULTS CENTERED WITH SEPARATOR LINES, USING F-STRINGS AND THE STRING .CENTER() METHOD

LINE_WIDTH = 95  # width used for centering and separator length

# INPUT: gather details from the user with \n after to have input prompt on a fresh line
full_name = input("Enter your first and last name:\n")
major = input("What is your college major?\n")
concept = input(
    "Identify or name a major concept or feature you want to learn using Python\n"
)
dream_job = input(
    "What is your dream job after completing your degree?\n"
)

# PROCESS: build sentences using f-strings
sentence1 = f"My name is {full_name}."
sentence2 = f"My current college major is {major}."
sentence3 = (
    f"The feature or concept I wish to learn about using Python is {concept}."
)
sentence4 = f"The dream job is to obtain is {dream_job}."

# OUTPUT: print a separating line before and after, and center the sentences
separator = "=" * LINE_WIDTH
print(separator)
print(sentence1.center(LINE_WIDTH))
print(sentence2.center(LINE_WIDTH))
print(sentence3.center(LINE_WIDTH))
print(sentence4.center(LINE_WIDTH))
print(separator)
# END PROGRAM

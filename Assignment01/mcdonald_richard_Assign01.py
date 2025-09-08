# PROGRAMMER: RICHARD KYLE MCDONALD
# PROGRAM NAME: COP 1000 – Assignment #01
# DATE WRITTEN: 09/08/2025
# FILENAME: mcdonald_richard_Assign01.py
# PROGRAM PURPOSE: PROMPT THE USER TO INPUT THEIR NAME, COLLEGE MAJOR AND A PYTHON BASED CONCEPT OF INTEREST
# PROGRAM PURPOSE: DISPLAY THE RESULTS CENTERED WITH SEPARATOR LINES, USING F-STRINGS AND THE STRING .CENTER() METHOD

LINE_WIDTH = 95  # width used for centering and separator length

# Helper: save output to a text file (overwrite each run so it’s up to date)
def save_output(filepath, lines):
    content = "\n".join(lines) + "\n"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

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

# OUTPUT: build lines, print them, then save to a TXT file
separator = "=" * LINE_WIDTH
lines = [
    separator,
    sentence1.center(LINE_WIDTH),
    sentence2.center(LINE_WIDTH),
    sentence3.center(LINE_WIDTH),
    sentence4.center(LINE_WIDTH),
    separator,
]

for line in lines:
    print(line)

save_output("Assignment01/mcdonald_richard_Assign01_output.txt", lines)
# END PROGRAM

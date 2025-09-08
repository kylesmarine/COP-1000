# PROGRAMMER: RICHARD KYLE MCDONALD
# PROGRAM NAME: COP 1000 – Assignment #02
# DATE WRITTEN: 09/08/2025
# FILENAME: mcdonald_richard_Assign02.py
# PROGRAM PURPOSE:
#   Ask for the user's name and the number of lions and tigers.
#   Calculate the total and the percentages for each animal.
#   Show a centered report using f-strings and the .center() method.

# Set a fixed width used to center text and draw separator lines
LINE_WIDTH = 60

# Helper to save to text file (overwrites each run)
def save_output(filepath, lines):
    # Join all lines with a newline character
    content = "\n".join(lines) + "\n"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

# input() shows a prompt and waits for the user to type and press Enter.
# save the answers in variables so we can use them later.
full_name = input("Enter your first and last name:\n")

# int() convert text to a whole number so we can do math.
lions = int(input("Enter the number of lions:\n"))
tigers = int(input("Enter the number of tigers:\n"))

# Total big cats is the sum of lions and tigers.
total = lions + tigers

# Avoid dividing by zero when there are no animals at all.
if total == 0:
    percent_lions = 0.0
    percent_tigers = 0.0
else:
    # Percent = part divided by whole (e.g., 8 / 20 = 0.40)
    percent_lions = lions / total
    percent_tigers = tigers / total

# Build all lines first so we can both print and save them
separator = "=" * LINE_WIDTH
lines = [
    separator,
    f"Local Zoo - Big Cats Report: By {full_name}".center(LINE_WIDTH),
    separator,
    f"Number of Lions: {lions}".center(LINE_WIDTH),
    f"Number of Tigers: {tigers}".center(LINE_WIDTH),
    f"Total Big Cats : {total}".center(LINE_WIDTH),
    separator,
    f"Lions: {percent_lions:,.2%}".center(LINE_WIDTH),
    f"Tigers: {percent_tigers:,.2%}".center(LINE_WIDTH),
    separator,
]

# Print to the screen
for line in lines:
    print(line)

# Save to a TXT file (overwrite to keep the latest results)
save_output("Assignment02/mcdonald_richard_Assign02_Output.txt", lines)

# END PROGRAM

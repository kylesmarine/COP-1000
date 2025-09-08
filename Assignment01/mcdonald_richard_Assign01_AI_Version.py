######################################################################
# PROGRAMMER: GPT5 - Guided by Richard Kyle McDonald
# PROGRAM NAME: COP 1000 – Assignment #01 (AI Version)
# DATE WRITTEN: 09/08/2025
# FILENAME: mcdonald_richard_Assign01_AI_Version.py
######################################################################

"""
This is a very simple, beginner‑friendly version of Assignment #01.

What it does (in plain steps):
1) Asks four questions using input().
2) Builds sentences using f-strings (formatted strings).
3) Wraps long sentences so they do not go past the width.
4) Centers each wrapped line using .center() so the text is in the middle.
5) Draws a separator line made of = signs before and after the text.

Notes for beginners:
- input(...) reads what the user types. We add "\n" to show a new line.
- .strip() removes any extra spaces at the start or end of what was typed.
- f"...{thing}..." lets us put variables inside the text easily.
- .center(width) returns a new string centered within the given width.

 Extra: Strings, literals, and variables (super simple):
 - A "string" is text inside quotes, like "Hello". It’s data made of letters.
 - A "literal" is a value written directly in the code:
     - String literal: "Hello", "="
     - Number (integer) literal: 85
 - A "variable" is a named box that holds a value, like name or WIDTH.
   We give the box a value using = (assignment), e.g., WIDTH = 85.
"""

# How wide the output area is. Try changing this to see the effect.
# WIDTH is a variable name (the box). 85 is a number literal we store in it.
WIDTH = 95

# Where to save the AI output each run (overwrite to keep latest)
OUTPUT_PATH = "Assignment01/mcdonald_richard_Assign01_AI_output.txt"


def save_output(filepath, lines):
    """Write the report lines to a text file, one per line."""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def wrap_text(text, width):
    """Very simple word-wrapping.

    Goal: return a list of lines where each line length <= width.
    How it works (beginner version):
    - Split the text into words by spaces.
    - Keep adding words to the current line until the next word would make it too long.
    - When it would be too long, start a new line.
    - Edge case: if one word is longer than width, split that single word.
    """
    words = text.split()  # split on spaces into a list of words
    lines = []
    current = ""

    for word in words:
        # If the word itself is longer than width, split it into chunks.
        if len(word) > width:
            # Finish the current line first.
            if current:
                lines.append(current)
                current = ""
            # Break the long word into pieces of size width.
            start = 0
            while start < len(word):
                chunk = word[start : start + width]
                lines.append(chunk)
                start += width
            continue  # move to the next word

        # If current line is empty, start with the word.
        if not current:
            current = word
        # Otherwise try to add a space + word, but only if it fits.
        elif len(current) + 1 + len(word) <= width:
            current += " " + word
        else:
            # Too long: push the current line and start a new one.
            lines.append(current)
            current = word

    # Add the last line if there is one.
    if current:
        lines.append(current)

    return lines


def main():
    # 1) Ask the user for their information.
    # input("...") shows a prompt. The text in quotes is a string literal.
    # .strip() removes extra spaces from the start and end of what was typed.
    name = input("Enter your first and last name:\n").strip()
    major = input("What is your college major?\n").strip()
    concept = input(
        "Identify or name a major concept or feature you want to learn using Python\n"
    ).strip()
    dream_job = input(
        "What is your dream job after completing your degree?\n"
    ).strip()

    # 2) Make a separator line using = repeated WIDTH times.
    # "=" is a string literal (just one equals sign). The * repeats it.
    # WIDTH is the number of times we repeat it. Example: "=" * 3 -> "==="
    separator = "=" * WIDTH

    # Build all lines first so we can both print and save them.
    report_lines = []
    report_lines.append(separator)

    # 4) Wrap each sentence to the width, then center each wrapped line.
    #    The .center(WIDTH) call makes the text appear in the middle.
    #    Below we use f-strings: f"My name is {name}."
    #      - The words inside quotes are string literals.
    #      - {name} is replaced with whatever the user typed (the variable value).

    sentence1 = f"My name is {name}."
    for line in wrap_text(sentence1, WIDTH):
        report_lines.append(line.center(WIDTH))

    # Another f-string: includes a string literal and the variable major.
    sentence2 = f"My current college major is {major}."
    for line in wrap_text(sentence2, WIDTH):
        report_lines.append(line.center(WIDTH))

    # A longer f-string: same idea—mix of literal text and the variable concept.
    sentence3 = (
        f"The feature or concept I wish to learn about using Python is {concept}."
    )
    for line in wrap_text(sentence3, WIDTH):
        report_lines.append(line.center(WIDTH))

    # One more: mixes literal text with the variable dream_job.
    sentence4 = f"The dream job is to obtain is {dream_job}."
    for line in wrap_text(sentence4, WIDTH):
        report_lines.append(line.center(WIDTH))

    # 5) Add the bottom separator line.
    report_lines.append(separator)

    # Print to screen
    for line in report_lines:
        print(line)

    # Save to file (overwrite to keep most recent)
    save_output(OUTPUT_PATH, report_lines)


# This says: only run main() when this file is executed directly.
# "__name__" is a built-in variable. When we run this file, it equals "__main__".
if __name__ == "__main__":
    main()

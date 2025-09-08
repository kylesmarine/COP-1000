######################################################################
# PROGRAMMER: GPT5 - Guided by Richard Kyle McDonald
# PROGRAM NAME: COP 1000 – Assignment #02 (AI Version)
# DATE WRITTEN: 09/08/2025
# FILENAME: mcdonald_richard_Assign02_AI_Version.py
# PURPOSE:
#   Ask for your name and for the number of lions and tigers.
#   Compute totals and percentages, then print a centered report.
#   Also save the same report to a TXT output file on every run.
#
# Beginner notes (vocabulary we are using):
# - String: text in quotes, e.g., "Hello" or "=\n". This is a string literal.
# - Number (integer) literal: a whole number written directly, e.g., 60.
# - Variable: a named box that holds a value, e.g., WIDTH = 60.
# - Assignment: the = sign stores a value in a variable, e.g., total = lions + tigers.
# - f-strings: formatted strings like f"Total: {total}" that insert variable values.
# - .center(width): centers a string within a given width by padding spaces.
# - Percent formatting: f"{value:,.2%}" turns 0.4 into "40.00%" (2 decimals).
######################################################################

# WIDTH controls the visual width used to center text and draw lines.
WIDTH = 60

# Where to store the AI output every time the program runs. Using 'w' when
# opening the file overwrites any previous run so this is always the latest.
OUTPUT_PATH = "Assignment02/mcdonald_richard_Assign02_AI_Output.txt"


def safe_int(text):
    """Convert input text to an int in a beginner-friendly way.

    If conversion fails (user typed non-numeric), return 0 instead of crashing.
    This keeps the program simple and safe for new users.
    """
    try:
        return int(text)
    except ValueError:
        return 0


def format_percent(value):
    """Format a decimal as a percentage string with two decimals.

    Example: value=0.4 -> returns "40.00%".
    The pattern ":,.2%" means:
      - ","  : use commas for thousands (not visible for small values)
      - ".2" : show two digits after the decimal point
      - "%"  : multiply by 100 and add the % symbol
    """
    return f"{value:,.2%}"


def build_report_lines(name, lions, tigers, width):
    """Return a list of text lines for the report (console + file).

    We build all output first so we can both print it and write it to a file.
    """
    lines = []

    # Separator is a string literal of '=' repeated "width" times using * (repeat).
    sep = "=" * width

    # Total is an integer calculation using + (addition).
    total = lions + tigers

    # Guard against division by zero when there are no animals.
    if total == 0:
        percent_lions = 0.0
        percent_tigers = 0.0
    else:
        # Percent = part / whole (e.g., 8 / 20 = 0.40 which is 40%).
        percent_lions = lions / total
        percent_tigers = tigers / total

    # Title block
    lines.append(sep)
    # f-string inserts the variable "name" into the string literal.
    lines.append(f"Local Zoo - Big Cats Report: By {name}".center(width))
    lines.append(sep)

    # Body lines with centered f-strings
    lines.append(f"Number of Lions: {lions}".center(width))
    lines.append(f"Number of Tigers: {tigers}".center(width))
    lines.append(f"Total Big Cats : {total}".center(width))
    lines.append(sep)

    # Percent formatting using :,.2% creates strings like "40.00%"
    lines.append(f"Lions: {format_percent(percent_lions)}".center(width))
    lines.append(f"Tigers: {format_percent(percent_tigers)}".center(width))
    lines.append(sep)

    return lines


def main():
    # =========================
    # INPUT (ask the user)
    # =========================
    # input() shows a prompt and waits; .strip() removes extra spaces at ends.
    name = input("Enter your first and last name:\n").strip()
    lions = safe_int(input("Enter the number of lions:\n"))
    tigers = safe_int(input("Enter the number of tigers:\n"))

    # =========================
    # BUILD OUTPUT LINES
    # =========================
    report_lines = build_report_lines(name, lions, tigers, WIDTH)

    # =========================
    # DISPLAY ON SCREEN
    # =========================
    for line in report_lines:
        print(line)

    # =========================
    # SAVE TO FILE (overwrite so it’s always the latest)
    # =========================
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        for line in report_lines:
            f.write(line + "\n")


if __name__ == "__main__":
    main()

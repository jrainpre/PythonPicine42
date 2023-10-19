# This time you have to make a real autonomous program, with a main, which takes
# a single string argument and displays the sums of its upper-case characters, lower-case
# characters, punctuation characters, digits and spaces.
# • If None or nothing is provided, the user is prompted to provide a string.
# • If more than one argument is provided to the program, print an AssertionError.
# Expected outputs:
# $>python building.py "Python 3.0, released in 2008, was a major revision that is not completely backwardcompatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020."
# The text contains 171 characters:
# 2 upper letters
# 121 lower letters
# 8 punctuation marks
# 25 spaces
# 15 digits
# $>
# Expected outputs: (the carriage return counts as a space, if you don’t want to return
# one use ctrl + D)
# $>python building.py
# What is the text to count?
# Hello World!
# The text contains 13 characters:
# 2 upper letters
# 8 lower letters
# 1 punctuation marks
# 2 spaces
# 0 digits
# $>


def count_uppercase(input_str) -> int:
    """Count the number of uppercase characters in a string"""
    return len([c for c in input_str if c.isupper()])


def count_lowercase(input_str) -> int:
    """Count the number of lowercase characters in a string"""
    return len([c for c in input_str if c.islower()])


def count_punctuation(input_str) -> int:
    """Count the number of punctuation characters in a string"""
    string_punctuation = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    return len([c for c in input_str if c in string_punctuation])


def count_spaces(input_str) -> int:
    """Count the number of spaces in a string"""
    return len([c for c in input_str if c.isspace()])


def count_digits(input_str) -> int:
    """Count the number of digits in a string"""
    return len([c for c in input_str if c.isdigit()])


def main():
    """Main function, takes a single string argument
      and displays the sums of its upper-case characters,
        lower-case, punctuation, digits and spaces."""
    import sys

    arg_error = "more than one argument is provided"
    argv = sys.argv
    argc = len(argv) - 1

    input_str = ''
    if argc == 0:
        try:
            print("What is the text to count?")
            input_str = input()
        except EOFError:
            pass
    else:
        input_str = argv[1]
    try:
        assert argc < 2, arg_error
    except AssertionError as error:
        print(f"AssertionError: {error}")
        sys.exit(1)

    print(f"The text contains {len(input_str)} characters:")
    print(count_uppercase(input_str), "upper letters")
    print(count_lowercase(input_str), "lower letters")
    print(count_punctuation(input_str), "punctuation marks")
    print(count_spaces(input_str), "spaces")
    print(count_digits(input_str), "digits")


if __name__ == "__main__":
    main()

import sys


def count_punctuation(text) -> int:
    """Count the number of punctuation marks in the text"""
    punctuation_str = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    return len([char for char in text if char in punctuation_str])


def count_spaces(text) -> int:
    """Count the number of spaces in the text"""
    return len([char for char in text if char.isspace()])


def count_digits(text) -> int:
    """Count the number of digits in the text"""
    print(count_digits.__doc__)
    return len([char for char in text if char.isdigit()])


def count_upper(text) -> int:
    """Count the number of upper case letters in the text"""
    return len([char for char in text if char.isupper()])


def count_lower(text) -> int:
    """Count the number of lower case letters in the text"""
    return len([char for char in text if char.islower()])


def print_counts(text):
    """Print the counts of the different char types in the text"""
    print(f"The text contains {len(text)} characters:")
    print(f"{count_upper(text)} upper letters")
    print(f"{count_lower(text)} lower letters")
    print(f"{count_punctuation(text)} punctuation marks")
    print(f"{count_spaces(text)} spaces")
    print(f"{count_digits(text)} digits")


def main():
    """main function
        1. checks if there is an argument
        2. takes input if there is no argument
        3. checks if there is more than one argument
        4. prints the counts of the different char types in the text"""
    try:
        argc = len(sys.argv)
        if argc < 2:
            try:
                s = input("What is the text to count?\n")
                s += "\n"
            except EOFError:
                pass
        elif argc == 2:
            s = sys.argv[1]
        assert argc < 3, "more than one argument is provided"
        print_counts(s)
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
    main()

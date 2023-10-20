import sys


def alphnum_space(s):
    """checks if a string only consits of alphanumeric characters and spaces"""
    return all([char.isalnum() or char.isspace() for char in s])


def convert_morse(s):
    """converts a string to morse code"""
    morse = {
        " ": "/",
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "0": "-----"
    }
    return "".join([morse[char.upper()] for char in s])


def main():
    """main function
    1. checks arguments
    2. checks argument is alphanumeric + space
    3. prints out the input string with help of morse dict"""
    try:
        argc = len(sys.argv)
        assert argc == 2, "the arguments are bad"
        s = sys.argv[1]
        assert alphnum_space(s), "the argument is not alphanumeric + space"
        print(convert_morse(s))
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
    main()

import sys
from ft_filter import ft_filter


def main():
    """main function
    1.checks the arguments count is 3
    2. checks the second argument is an integer
    3. splits the first argument into words
    4. filters the words with length greater than the input integer
    5. prints the filtered words"""
    try:
        argc = len(sys.argv)
        assert argc == 3, "the arguments are bad"
        try:
            n = int(sys.argv[2])
        except ValueError:
            print(ValueError.__name__ + ": second argument is not an integer")
            sys.exit(1)
        s = sys.argv[1]
        words = s.split()
        filtered_words = ft_filter(lambda x: len(x) > n, words)
        print(list(filtered_words))
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)


if __name__ == "__main__":
    main()

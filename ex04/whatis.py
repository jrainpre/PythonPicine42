
import sys

argv = sys.argv
argc = len(argv) - 1
ARG_ERROR = "more than one argument is provided"
VALUE_ERROR = "AssertionError: argument is not an integer"

if argc == 0:
    sys.exit(0)

try:
    assert argc < 2, ARG_ERROR
except AssertionError as error:
    print(f"AssertionError: {error}")
    sys.exit(1)
try:
    num = int(argv[1])
except ValueError:
    print(VALUE_ERROR)
    sys.exit(1)
if num % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")

# Create a script that takes a number as argument, checks whether it is odd or even,
# and prints the result.
# If more than one argument is provided or if the argument is not an integer, print an
# AssertionError.
# Expected output:
# $> python whatis.py 14
# I'm Even.
# $>
# $> python whatis.py -5
# I'm Odd.
# $>
# $> python whatis.py
# $>
# $> python whatis.py 0
# I'm Even.
# $>
# $> python whatis.py Hi!
# AssertionError: argument is not an integer
# $>
# $> python whatis.py 13 5
# AssertionError: more than one argument is provided

import sys

argv = sys.argv
argc = len(argv) -1

if argc == 0:
	sys.exit(0)

try:
    assert argc  <2, "more than one argument is provided"
except AssertionError as error:
    print(f"AssertionError: {error}")
    sys.exit(1)
try:
	num = int(argv[1])
except ValueError:
	print("AssertionError: argument is not an integer")
	sys.exit(1)
if num % 2 == 0:
	print("I'm Even.")
else:
	print("I'm Odd.")

from NULL_not_found import NULL_not_found
Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ''
Fake = False
NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))



# Expected output:
# $>python NULL_not_found.py | cat -e
# Nothing: None <class 'NoneType'>$
# Cheese: nan <class 'float'>$
# Zero: 0 <class 'int'>$
# Empty: <class 'str'>$
# Fake: False <class 'bool'>$
# Type not Found$


# Nothing:  None <class 'NoneType'>$
# Cheese:  nan <class 'float'>$
# Zero:  0 <class 'int'>$
# Empty:  <class 'str'>$
# Fake:  False <class 'bool'>$
# Type not found$
# 1$

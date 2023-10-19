# Return 0 if it goes well and 1 in case of error.
# Your function needs to print all types of NULL.


def isNaN (object: any) -> bool:
	if (object != object):
		return True
	return False

def NULL_not_found(object: any) -> int:
	if object == None:
		print("Nothing:", None, type(None))
	elif isNaN(object):
		print("Cheese:", "nan", float)
	elif object == 0 and not object is False:
		print("Zero:", 0, int)
	elif object == '':
		print("Empty:", str)
	elif object is False:
		print("Fake:", False, bool)
	else:
		print("Type not found")
		return 1
	return 0

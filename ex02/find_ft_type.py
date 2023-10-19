# Write a function that prints the object types and returns 42.
# Here’s how it should be prototyped:
# def all_thing_is_obj(object: any) -> int:
# #your code here






def all_thing_is_obj(object: any) -> int:
	if type(object) == list:
		print("List :", type(object))
	elif type(object) == tuple:
		print("Tuple :", type(object))
	elif type(object) == set:
		print("Set :", type(object))
	elif type(object) == dict:
		print("Dict :", type(object))
	elif type(object) == str:
		print(f"{object} is in the kitchen :", type(object))
	else:
		print("Type not found")
	return 42
	
	


	





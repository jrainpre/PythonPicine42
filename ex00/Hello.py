ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}
#your code here

ft_list[1] = "World!"
ft_tuple = ("Hello", "Austria!")
ft_set.remove("tutu!")
ft_set.add("Vienna!")
ft_dict["Hello"] = "42Vienna"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

# $>python Hello.py | cat -e
# ['Hello', 'World!']$
# ('Hello', 'France!')$
# {'Hello', 'Paris!'}$
# {'Hello': '42Paris!'}$
# $>
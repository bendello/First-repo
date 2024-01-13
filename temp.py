my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(my_dict["name"])  # Виведе 'Alice'
my_dict.update({"email": "alice@gmail.com"})
print(my_dict)
my_dict.pop("email")
print(my_dict)
gender = my_dict.get("gender")
print(my_dict)
a = {1, 2, 3}
b = {3, 4, 5}
print(a.intersection(b))  # {3}
print(a & b)  # {3}
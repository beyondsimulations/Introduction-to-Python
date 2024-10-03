# Create a dictionary with the following information about yourself: name, age, city
i_am = {"name": "Tobias", "age": 30, "city": "Hamburg"}

i_am["color"] = "red"
i_am["food"] = "lasagne"
print(i_am)

city = i_am.pop("city")
print(i_am)

i_am = {"name": "Tobias", "age": 30, "city": "Hamburg"}
print(f"My name is {i_am['name']}.")
# Create a dictionary with the following information about yourself: name, age, city
i_am = {
    "name": "Tobias",
    "age": 30,
    "city": "Hamburg",
    "color": "red",
    "food": "lasagne",
    "name": "Test",
}
print(i_am)
city = i_am.pop("city")
print(i_am)

print(f"My name is {i_am['name']} and I am {i_am['age']}.")

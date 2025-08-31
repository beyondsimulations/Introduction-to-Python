# TODO: Create a phonebook application
# - Create a dictionary to store names and phone numbers.
# - Add at least 5 entries to the dictionary in the initialisation. 
# - Write a function to look up a phone number by name based on a user input.
# - Write a function to update a phone number based on a user input.
# - Write a function to delete an entry by name based on a user input.
# - Write a function that saves the phonebook to a text file.
# - Write a small program that asks for a user input on whether the user wants to add, remove, or update a phone number.
# - After each operation, the phonebook should be saved to the text file.

phonebook = {
    "Hans Zimmer": "1234567890",
    "John Williams": "0987654321",
    "Ennio Morricone": "1122334455",
    "Ludwig van Beethoven": "6677889900",
    "Wolfgang Amadeus Mozart": "1234123412"
}

def lookup_phone_number(name):
    return phonebook.get(name, "Name not found")

def update_phone_number(name, number):
    phonebook[name] = number
    save_phonebook()
    print(f"Updated {name}'s number to {number}")

def delete_phone_number(name):
    if name in phonebook:
        del phonebook[name]
        save_phonebook()
        print(f"Deleted {name} from the phonebook")
    else:
        print("Name not found")

def save_phonebook():
    with open("phonebook.txt", "w") as f:
        for name, number in phonebook.items():
            f.write(f"{name}: {number}\n")

def add_phone_number(name, number):
    phonebook[name] = number
    save_phonebook()
    print(f"Added {name} with number {number} to the phonebook")

def main():
    while True:
        action = input("What would you like to do? (lookup/add/update/delete/quit): ").lower()
        
        if action == "lookup":
            name = input("Enter the name to lookup: ")
            print(lookup_phone_number(name))
        elif action == "add":
            name = input("Enter the name to add: ")
            number = input("Enter the phone number: ")
            add_phone_number(name, number)
        elif action == "update":
            name = input("Enter the name to update: ")
            number = input("Enter the new phone number: ")
            update_phone_number(name, number)
        elif action == "delete":
            name = input("Enter the name to delete: ")
            delete_phone_number(name)
        elif action == "quit":
            break
        else:
            print("Invalid action. Please try again.")

main()




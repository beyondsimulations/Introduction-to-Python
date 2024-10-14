# The encoded message is:
secret_message = ".tnega terces a sa slliks ym sevorpmi erutcel oN"

# a) Reverse the string
decoded_message = secret_message[::-1]
print("a) Reversed:", decoded_message)

# b) Remove the period at the end
decoded_message = decoded_message[:-1]
print("b) Period removed:", decoded_message)

# c) Replace 'No' with 'This'
decoded_message = decoded_message.replace("No", "This")
print("c) 'No' replaced:", decoded_message)

# d) Convert the string to title case
decoded_message = decoded_message.title()
print("d) Title case:", decoded_message)

# e) Add an exclamation mark at the end of the sentence
decoded_message += "!"
print("e) Exclamation added:", decoded_message)

# f) Count how many times the letter 's' appears in the decoded message (upper and lower case)
s_count = decoded_message.lower().count('s')
print(f"f) The letter 's' appears {s_count} times in the decoded message")

print("\nFinal decoded message:", decoded_message)
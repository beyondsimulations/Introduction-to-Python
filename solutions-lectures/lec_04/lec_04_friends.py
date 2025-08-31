# You have a list of friends from two different groups
friends_group_1 = {"Neo", "Morpheus", "Trinity", "Cypher"}
friends_group_2 = { "Smith", "Apoc", "Cypher", "Morpheus"}

inter = friends_group_1.intersection(friends_group_2)
print(inter)

uni = friends_group_1.union(friends_group_2)
print(uni)

print(len(inter))

for name in uni:
    print(name)

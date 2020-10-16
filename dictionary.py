# dogs = {"Fido":8, "Sally":17, "Sean":2}
# print(dogs)

# # call 
# print(dogs["Fido"])

# # delete
# del(dogs["Fido"])
# print(dogs)

# # add
# dogs["Sarah"] = 6
# print(dogs)

# #update
# dogs["Sean"] = 100
# print(dogs)

# #all types
# dogs["John"] = True
# print(dogs)

#Exercise
# I have provided you with two lists. words and definitions
# Create a dictionary called cooldictionary where you use words for keys and definitions for values

# words = ["name", "age", "status"]
# definitions = ["Nina", 15, "ok"]
# cooldictionary = {
#     words[0]:definitions[0],
#     words[1]:definitions[1],
#     words[2]:definitions[2]
# }
# print(cooldictionary)

words = ["name", "age", "status"]
definitions = ["Nina", 15, "ok"]
cooldictionary = {}

for i in words:
    for j in definitions:
        cooldictionary[i] = j
print(cooldictionary)

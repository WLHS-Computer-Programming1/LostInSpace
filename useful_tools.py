'''
Name: Brandon Smith
Date: 11/21/24
Description: Some useful tools for the text adventure that we may not
full explore in class or be tested on
'''

# List

# Store multiple items of the same or different types in one variable
# Format: my_list = [item1, item2, item3,....,last_item]
# Location, called index, starts at 0
# To get first item, my_list[0]

character_info = ["Norman",7,"Cat","Black","Yellow",4,"Quirky"]
for item in character_info:
    print(item)

name = character_info[0]
print(f"Name: {name}")
num_legs = character_info[5]
print(f"Number of legs: {num_legs}")

def leg_change(info,leg_number):
    info[5] = leg_number
    return info

character_info = leg_change(character_info,3)
num_legs = character_info[5]
print(f"Number of legs: {num_legs}")


# Dictionary
# Allows you to store data as key-value pairs. Basically, your index, called a key can
# be a word, not a number
# Format: my_dictionary = {key1:value1,key2:value2,key3:value3} etc.
# To get an item, my_dictionary[key]

character_dictionary = {
    "Name":"Norman",
    "Age":7,
    "Species":"Cat",
    "Color":"Black",
    "Eye Color":"Yellow",
    "num_legs":4,
    "adj_1":"Quirky",
    "inventory":["key","meds","flashlight"]
}
print(character_dictionary["Species"])


# Sleep
# import sleep is needed at top; delays next line of code for specified time
# Format: time.sleep(time_in_seconds)
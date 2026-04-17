# create an empty dictionary .Allow 4 friends to enter their favpurite language as value and use key as theri names.Assume that the names are unique

fav_language = {}

name1 = input("Enter friend 1 name: ")
lang1 = input("Enter their favourite language: ")
fav_language[name1] = lang1

name2 = input("Enter friend 2 name: ")
lang2 = input("Enter their favourite language: ")
fav_language[name2] = lang2

name3 = input("Enter friend 3 name: ")
lang3 = input("Enter their favourite language: ")
fav_language[name3] = lang3

name4 = input("Enter friend 4 name: ")
lang4 = input("Enter their favourite language: ")
fav_language[name4] = lang4

print("Favourite Languages:", fav_language) 
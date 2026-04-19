# remove word and strip spaces 
def remove():
    text = input("Enter a sentence")
    word  = input("Enter word to remove:")
    result = text.replace(word,"").strip() # in repace it always contain 2 value like what u want to remove and what do u want to add so if we dont want anything we keep it ""
    print("Result:", result)
remove()
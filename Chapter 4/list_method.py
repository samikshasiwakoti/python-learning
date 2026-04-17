text = ["apple", "orange", 5, 345.06, False, "Samii"]

text.append("samiiksha")
text.insert(2, 6)# insert 6 in index 2
text.remove(5)
text.reverse()

print(text.count("apple"))#bthose method which can return value can be placed inside print
print(text.index("orange"))
print(text.pop())   # removes last element and prints it
print(text)

l1 = [7,4,8,0,1,2]
l1.sort()
print(l1)
s = { 1, 5, 32, 54, 5, 5, 5, "Samii"}
print(s,type(s))
s.add(5566)
print(s,type(s))
print(len(s))
s.remove(32)
print(s)

s1 = {1,2,6,8,9,10}
s2 = {7,6,1,11,12,13}
print(s1.union(s2))
print(s1.intersection(s2))

s3 ={5,7,9,10,11,12}
print(s3.union({8,11})) # if duplicate is there it will ignored and if new value is there it would add
print(s3.intersection({7,9}))

s3 = {1, 2, 3}

print(s3.intersection({7, 9})) # it gives empty set
print({1,2}.issubset(s1)) # if it is subset than true

print(s1.issuperset({1,2}))
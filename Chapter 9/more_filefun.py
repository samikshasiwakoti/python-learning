st = " Hey how u doing"
f = open("file.txt","w")
f.write(st)
print(st)
f.close()

with open("file.txt","w") as f:
    f.write("hello")

with open("file.txt","r") as f:
    print(f.read())
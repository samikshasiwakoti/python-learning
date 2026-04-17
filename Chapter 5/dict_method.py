
d ={} # empty dictionary

marks = {
    "samiksha" : 100,
    "asmita" : 200,
    "samii"  : 150,
    0:"samiksha"
}
print(marks.items())
print(marks.keys())
marks.update({"samiksha": 170, "asmita": 300})
print(marks)
print(marks.get("samii"))
print(marks.pop('asmita'))
print(marks.popitem())
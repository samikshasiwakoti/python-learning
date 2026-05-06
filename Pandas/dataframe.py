import pandas as pd
# data = {

#     "Name":["samiksha","Asmita","Samii","Asmii"],
#     "Age" :[20,21,18,19]
# }



data ={
    "Name":["Sami","Asmii",],
    "Age" :[21,19,]
}

df = pd.DataFrame(data,index=['Product A','Product B'])
print(df)
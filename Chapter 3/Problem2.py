#Write a program to fill in a letter template given below with name and date

letter ='''Dear<|Name|>
,you are selected!
<|Date|>'''

print(letter.replace("<|Name|>","samiksha").replace( "<|Date|>","24April"))
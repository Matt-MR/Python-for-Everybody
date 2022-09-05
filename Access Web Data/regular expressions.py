import re 

file = open("c:/Users/a00537061/OneDrive - ONEVIRTUALOFFICE/Desktop/Code/Python for Everybody Specialization/Access Web Data/regex_sum_42.txt")
fhandle = file.read()

numlist = re.findall("[0-9]+", fhandle)

for num in numlist:
    number = int(num)
    print(number)




#y = re.findall("[0-9]+", fhandle)
#print(y)
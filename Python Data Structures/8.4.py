fname = input("Enter the name of the file: ")
fh = open(fname)

lst = []

for line in fh:
    data = line.split()
    
    for data in data:
        if data not in lst:
            lst.append(data)

print(sorted(lst))
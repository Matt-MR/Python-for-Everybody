fname = input("Enter file name: ")
fh = open(fname)
count = 0

for line in fh:
    if line.startswith("From "):
        count = count + 1
        data = line.split()
        print(data[1])
        continue
    
print("There were", count, "lines in the file with From as the first word")

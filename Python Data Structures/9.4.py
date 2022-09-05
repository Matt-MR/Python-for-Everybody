##  I am lost on this ＞﹏＜
# code below is the answer

fname = input("Enter the file name:")
fh = open(fname)

best = dict()

for line in fh:
    if line.startswith("From "):
        data = line.split()
        best[data[1]] = best.get(data[1], 0) + 1

largest = None
largest_author = None

for key in best:
    if largest is None: largest = best[key]

    if largest < best[key]:
        largest = best[key]
        largest_author = key

print(largest_author, largest)


#############################################################
# Trying to understand 

fname = input("Enter the file name:")
if len(fname) < 1: 
    fname = "mbox-short.txt"
fh = open(fname)

di = dict()

for line in fh:
    if line.startswith("From "):
    	data = line.split()
        key = data[1]
        print(key)
    for word in key:
        di[key] = di.get(key, 0) + 1
        
print(di)
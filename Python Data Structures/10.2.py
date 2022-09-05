name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

d = dict()

for line in handle:
    if line.startswith("From "):
        data = line.split()
        time = data[5]
        hour = time[0:2]
        d[hour] = d.get(hour, 0) + 1

lst = list(sorted(d.items()))

for k, v in lst:
    print(k, v)

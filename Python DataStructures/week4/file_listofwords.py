fname = input("Enter file name: ")
fh = open(fname,'r')
lst = list()
for line in fh:
    line=line.rstrip()
    words=line.split()
    for word in words:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)

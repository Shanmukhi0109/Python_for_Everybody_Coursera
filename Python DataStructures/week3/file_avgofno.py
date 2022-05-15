count=0
values=0
fname = input("Enter file name: ")
fh = open(fname,'r')
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count=count+1
    index=line.find('0')
    values=values+float(line[index:])
print("Average spam confidence:",values/count)

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
senderlist=list()
count=dict()
for line in handle:
    if line.startswith("From "):
        words=line.split()
        senderlist.append(words[1])
for i in senderlist:
     count[i]=count.get(i,0)+1
bigword=None
bigcount=None
for k,v in count.items():
    if bigword==None or v>bigcount:
        bigword=k
        bigcount=v
print(bigword,bigcount)

    

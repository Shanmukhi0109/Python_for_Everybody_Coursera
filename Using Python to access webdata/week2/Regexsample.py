import re
file=open("text.txt",'r')
numslist=list()
for line in file:
    num=re.findall('[0-9]+',line)
    if len(num)==0: continue
    for i in num:
        numslist.append(float(i))
print(sum(numslist))

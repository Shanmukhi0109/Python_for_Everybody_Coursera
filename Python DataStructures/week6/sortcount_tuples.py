name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
count_dict=dict()
for line in handle:
    if line.startswith("From "):
        line=line.rstrip()
    	words=line.split()
    	req_word=words[-2]
    	time=req_word.split(":")
    	hour=time[0]
        count_dict[hour]=count_dict.get(hour,0)+1
sorted_dict=sorted(count_dict.items())
for h,c in sorted_dict:
    print(h,c)

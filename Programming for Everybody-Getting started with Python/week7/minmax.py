largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        	break
    try:
        num=int(num)
    	if smallest is None and largest is None:
        	smallest=num
        	largest=num
    	elif num<smallest:
        	smallest=num
    	elif num>largest:
        	largest=num
    except:
        print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)

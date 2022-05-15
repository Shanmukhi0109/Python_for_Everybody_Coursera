score = input("Enter Score: ")
fscore=float(score)
if fscore>=0.9 and fscore<=1.0:
    print("A")
elif fscore>=0.8 and fscore<0.9:
    print("B")
elif fscore>=0.7 and fscore<0.8:
    print("C")
elif fscore>=0.6 and fscore<0.7:
    print("D")
elif fscore<0.6 and fscore>=0:
    print("F")
else:
    print("Value out of range")

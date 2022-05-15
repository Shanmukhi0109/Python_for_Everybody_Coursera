hrs = input("Enter Hours:")
h = float(hrs)
rate=input("Enter Rate:")
r=float(rate)
if h<=40:
    grosspay=h*r
else:
    grosspay=40*r+(h-40)*1.5*r
print(grosspay)

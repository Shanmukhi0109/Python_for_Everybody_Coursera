import urllib.request
from bs4 import BeautifulSoup

url =input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')
tags = soup('span')
count=0
sum=0
for tag in tags:
	for value in tag:
		sum=sum+float(value)
		count=count+1
print("Count:",count)
print("Value sum:",sum)

'''
Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_1533771.html (Sum ends with 35)
'''

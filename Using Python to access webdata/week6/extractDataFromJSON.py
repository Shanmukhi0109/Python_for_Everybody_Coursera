import urllib.request, urllib.parse, urllib.error
import json
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sum1=0

url=input('Enter- ')
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print('Retrieved', len(data), 'characters')
print(data.decode())

info = json.loads(data)

for item in info["comments"]:
    value=item['count']
    sum1=sum1+int(value)
print(sum1)

'''
Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_1533774.json (Sum ends with 63)
'''

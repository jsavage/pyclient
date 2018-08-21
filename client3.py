#!/usr/bin/python27
import http.client
#Level 1
print("running...")
conn1 = http.client.HTTPConnection("172.31.38.164")
conn1.request("GET", "/")
r1 = conn1.getresponse()
print(r1.status, r1.reason)
data1 = r1.read()
print(data1)
conn1.close()

#Level 2
conn2 = http.client.HTTPConnection("172.31.38.164")
conn2.request("GET", "/"+data1)
r2 = conn2.getresponse()
print(r2.status, r2.reason)
data2 = r2.read()
print(data2)
conn2.close()


#Level 3

import hashlib
from random import randint
conn3 = http.client.HTTPConnection("172.31.38.164:21337")
for x in range (100,199):
	dk = hashlib.pbkdf2_hmac('sha256', b'bsadg2342bfeds235sge2', b'12345', 100)
	seccode = dk.hex()
	print(seccode)
	conn3.request("GET", "/"+seccode)
	print("Trying " + seccode)
	r3 = conn3.getresponse()
	print(r3.status, r3.reason)
	data3 = r3.read()
	#print(data3)
conn3.close()






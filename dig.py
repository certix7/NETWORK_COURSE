import subprocess


R = '\x1b[31m'
G = '\x1b[1;32m'

hint="nano /etc/resolv.conf"+G
print(R + "_____________________________________________ " + "\n")
print("remember\n--------------\n","dig +noall +answer +norecurse #dns host# A\n",hint)
print()
#######################


i=input ("put your host :")
dns="8.8.8.8"

a=["dig +noall +answer {0} A".format(i),
"dig +noall +answer {0} CNAME".format(i)
,"dig +noall +answer {0} NS".format(i)
,"dig +noall +answer {0} MX".format(i)
,"dig +noall +answer @{} {} ANY".format(dns,i)
,"dig +noall +answer {0} ANY".format(i),]


"dnsrecon -d {0}".format(i)
"dnsrecon -d {0} -n “8.8.8.8 | 8.8.4.4”".format(i)

v=0
for x in a:
	v+=1
	print(str(v) +"-"+x)


print(G + "_____________________________________________ ")

com=subprocess.call("dig +noall +answer {0} ANY".format(i), shell=True)
print(com)


# 208.67.222.222+208.67.220.220 

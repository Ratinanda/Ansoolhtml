import sys
#arg1=sys.argv[1]
arg1="world"
f=open("resolv.conf.txt","rt")
for line in f:
    if arg1 in line:
        print(line)
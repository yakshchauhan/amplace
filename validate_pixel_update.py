import sys

print(sys.argv)

with open(sys.argv[0],'r+') as f:
    print(f.read())
    f.seek(0)
    with open("log.txt","w") as lo:
        for i in f.readlines():
            lo.write(i)
exit(-1)

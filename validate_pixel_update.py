import sys

print(sys.argv[1:])

with open("pixel_update.json",'r+') as f:
    print(f.read())
    f.seek(0)
    with open("log.txt","w") as lo:
        for i in f.readlines():
            lo.write(i)


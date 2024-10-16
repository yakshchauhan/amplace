import sys

print(sys.argv[1:])

with open(sys.argv[1:],"r+") as f:
    print(f.read())

    with open("log.txt","w") as lo:
        lo.writelines(f.readlines())

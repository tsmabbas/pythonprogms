from sys import argv

print("Hello", argv[1])

# tsmab@python:~/pythonprogms$ python3 argvdemo.py 'John Smith'

for filename in argv[1:]:
    with open(filename, 'r') as f:
        lines = f.readlines()
    lines.insert(0, filename.upper())
    lines.insert(1, "Auther: J. Smith \n")
    with open(filename, w) as f:
        f.writelines(lines)
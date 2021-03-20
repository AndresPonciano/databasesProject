import re

file1 = open('data.txt')
file2 = open('data2.txt', 'a')
lines = file1.readlines()

for line in lines:
    # print(line)
    confName = re.search("->\s[A-Za-z\s\/,]*", line)
    # file2.write(confName.match)
    # print(confName.start())
    print(line[confName.start()+3:])
    realConfName = line[confName.start()+3:]
    file2.write(realConfName)

file1.close()
file2.close()

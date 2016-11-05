line = input()
i = 0
massive = []
while line[i] != '.':
    massive.append(ord(line[i]))
    i += 1
massive = sorted(massive)
line = ''
for i in range(len(massive)):
    line += str(chr(massive[i]))
line += '.'
print(line)

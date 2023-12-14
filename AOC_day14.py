lines = [list(line.strip()) for line in open('input14.txt')]
def move(lines):
    for _ in range(len(lines)):
        for i in range(1,len(lines)):
            for j in range(len(lines[i])):
                if lines[i][j] == 'O' and lines[i-1][j] == '.':
                    lines[i][j], lines[i-1][j] = '.', 'O'
    return lines
c = {}
i,iters = -1, 1000000000
while (i:=i+1) < iters:
    for _ in range(4):
        lines = list((map(list,zip(*move(lines)[::-1]))))
    i = iters - (iters - i) % (i - c[str(lines)]) if str(lines) in c else i
    c[str(lines)] = i
print(sum([line.count('O')*(len(lines)-i) for i,line in enumerate(lines)]))
#Not the fastest code but still works

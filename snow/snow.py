appearances = [0]
x=0
y=0

with open("input.txt", "r") as input:
    v, e = map(int, input.readline().split())
    appearances = [0]*v #vertex갯수만큼 cell 선언

    for line in input:
        u, v = map(int, line.split())
        appearances[u - 1] += 1  # u 정점의 등장 횟수 증가
        appearances[v - 1] += 1  # v 정점의 등장 횟수 증가


appearances = sorted(appearances, reverse= True)

max_count = appearances[0]

i = 0
while max_count == appearances[i]:
    i += 1

if i == 1:
    x=appearances[0]
else:
    y = appearances[0]-1

second_max = appearances[i]
second_count = 0

if second_max != 1:
    while i<v and second_max == appearances[i] :
        i += 1
        second_count += 1
    if second_count == 1:
        x = second_max
    else:
        y = second_max-1
else:
    x = appearances[0]
    y = appearances[0]-1

with open("output.txt", "w") as output:
    output.write(str(x)+" "+str(y))
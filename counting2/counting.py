with open("input.txt", "r") as input:
    n, k = map(int, input.readline().split())
    arr = list(map(int, input.readline().split()))

#k+1개의 array가 존재하는지 확인 
check =[1]
for i in range(1,n) :
    if 2*arr[i]- arr[i-1] > 0 :
        check.append(1)
    else:
        check.append(0)


count = 0

for i in range(n-k):
    flag = True
    for j in range(k):
        if check[i+j] == 0:
            flag = False 
            break
    if flag:
        count += 1

with open("output.txt","w") as output:
    output.write(str(count))

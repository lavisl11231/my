import math

maxNum = 1000000
primeList = [2]
for num in range(3, maxNum+1):
    sqt = int(math.sqrt(num))
    primeFlag = 0
    for i in range(2, sqt+1):
        if num % i == 0:
            primeFlag = 1
    if primeFlag == 0:
        primeList.append(num)

print(f'Total count:{len(primeList)}')
primeList = [str(num) for num in primeList]
primeListString = ' '.join(primeList)

with open('prime.txt', mode='w') as f:
    f.write(primeListString)
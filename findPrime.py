# 找质数，计算方法：一个大于2的正整数不能被小于它的其他质数整除即为质数
primeList = [2]
for num in range(3, 100000):
    primeLength = len(primeList)
    i = 1
    for prime in primeList:
        if num % prime == 0 and i != primeLength:
            break
        elif num % prime != 0 and i == primeLength:
            primeList.append(num)
        else:
            i = i + 1
print(f'Total count:{len(primeList)}')
primeList = [str(num) for num in primeList]
primeListString = ' '.join(primeList)

with open('prime.txt', mode='w') as f:
    f.write(primeListString)

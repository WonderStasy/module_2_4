num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
primes = []
not_primes = []
a = 0
for i in range(2, len(num) + 1):
    for j in range(2, i):
        if i % j == 0:
            a += 1
    if a == 0:
        primes.append(i)
    else:
        a = 0
        not_primes.append(i)
print('primes: ', primes)
print('not primes: ', not_primes)
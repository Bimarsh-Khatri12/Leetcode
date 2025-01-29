import math
def countPrime(num):
    if num <= 1:
        return 0
    prime = [True] * num
    
    prime[0] = prime[1] = False
    
    for i in range(2,int(math.sqrt(num))+1):
        if prime[i]:
            for j in range(i*i,num,i):
                prime[j] = False
    
    return sum(prime)

print(countPrime(2))
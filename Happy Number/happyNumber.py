def happyNumber(n):
    visit = set()
    
    def next_number(n):
        sum = 0
        while n:
            sum = sum + (n % 10) **2
            n = n//10
        return sum
    
    while n not in visit:
        visit.add(n)
        
        n = next_number(n)
        
        if n == 1:
            return True
    return False

print(happyNumber(19))
        
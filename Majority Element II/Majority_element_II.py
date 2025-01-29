#Hashmap
def majorityelement(nums):
    arr= []
    l = len(nums)//3
    c = Counter(nums)
    for k,v in c.items():
        if(c>l):
            arr.append(k)
    return arr

def majority_element(nums):
    m1 = None
    m2 = None
    c1 = c2 = 0
    for num in nums:
        if(m1 is not None and m1 == num):
            c1+=1
        elif(m2 is not None and m2 == num):
            c2+=1
        elif(m1 == None):
            m1 = num
            c1+=1
        elif(m2 == None):
            m2 = num
            c2+=1
        else:
            c1-=1
            c2-=1
            if(c1 == 0):
                m1 == None
            if(c2 == 0):
                m2 == None
    c1 = c2 = 0
    arr = []
    l = len(nums)//3
    for num in nums:
        if(m1 == num):
            c1+=1
        elif(m2 == num):
            c2+=1
    if(c1>l):
        arr.append(m1)
    elif(c2>l):
        arr.append(m2)
    return arr



def tsearch(ar, target, left, right):
    #base condition #list is empty 
    if left > right: 
        return -1 
    #logic 
    mid1 = left + ((right - left) // 3)    
    mid2 = right - ((right - left) // 3)    

    if target == ar[mid1]:
        return mid1 
    elif target == ar[mid2]:
        return mid2 
    else: 
        #reduce the list either as left, middle, right 
        if target < ar[mid1]: 
            return tsearch(ar, target, left, mid1 - 1) # left list 
        elif target > ar[mid2]:
            return tsearch(ar,target,mid2+1,right) #right list 
        else:
            return tsearch(ar,target,mid1+1,mid2-1) #middle list excludes mid1 and mid2 
def solve():
    #N=len(ar)#8
    ar = [2, 3, 4, 5, 6, 7, 8, 10]
    target=  13 # 13 # 1 # 9 # 5 # 4 # 8 
    index = tsearch(ar, target,0,len(ar)-1)
    print(index)
solve()

#time complexity: 
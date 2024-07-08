def bsearch(ar, target):
    N = len(ar)
    left, right = 0, N-1
    while left <= right: 
        mid = (left + right) // 2 
        if target == ar[mid]:
            return mid 
        elif target < ar[mid]:
            right = mid - 1
        else:   
            left = mid + 1
    return -1 

def solve():
    #N=len(ar)#8
    ar = [2, 3, 4, 5, 6, 7, 8, 10]
    target= 13 # 1 # 9 # 5 # 4 # 8 
    index = bsearch(ar, target)
    print(index)

solve()

#time complexity: 
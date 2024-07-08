def lsearch(ar,target):
    N=len(ar)
    for I in range(N):
        if ar[I] == target:
            return I 
    return -1

def solve():
    #N=len(ar)#8
    ar = [7, 4, 3, 5, 8, 10, 2, 6]
    target=9 #6 #5 #4 #2
    index = lsearch(ar, target)
    print(index)

solve()

#time complexity: O(N) 
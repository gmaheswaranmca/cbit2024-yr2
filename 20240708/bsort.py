def bsort(ar):
    N = len(ar)

    while True:
        isSwapped = False 
        #pass code 
        for I in range(N-1): # 0 .. N-2 
            if ar[I] > ar[I+1]: #comparison of adj elements 
                ar[I],ar[I+1] = ar[I+1],ar[I] #swap 
                isSwapped = True 
        if not isSwapped:
            break
    # the elements sorted 
def solve():
    #N=len(ar)#8
    #ar = [7, 4, 3, 5, 8, 10, 2, 6]
    #ar = [3, 5, 8, 10]
    ar = [100, 88, 90, 45, 85, 67, 110, 40, 77, 92, 13, 62]
    print('Before sort:',ar)
    bsort(ar)
    print('After sort:',ar)
    
solve()

#time complexity: O(N^2) for average and worst cases, O(N) for best case [sorted data]
#space complexity: O(1)
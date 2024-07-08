def isort(ar):
    N = len(ar)
    for I in range(1,N): #initially we have first element sub list as sorted, all elements are in unsorted list.
        target = ar[I]  # initialize first element of the unsorted element 
        tindex = I      # assume the position for the first element is same 
        sindex = I - 1  
        while sindex >= 0 and target < ar[sindex]: # check the position for target element 
            ar[sindex+1] = ar[sindex] # parrallel run for shifting right for insertion of target element 
            sindex -= 1     # scan previous elements in the sorted list 
            tindex -= 1     # change the position of the tareget element 
        if tindex != I: # insertion we done. the shifting right happened before during finding the pos. 
            ar[tindex] = target 
        
    #elements sorted 

def solve():
    #N=len(ar)#8
    #ar = [7, 4, 3, 5, 8, 10, 2, 6]
    #ar = [3, 5, 8, 10]
    ar = [100, 88, 90, 45, 85, 67, 110, 40, 77, 92, 13, 62]
    print('Before sort:',ar)
    isort(ar)
    print('After sort:',ar)
    
solve()

#time complexity:  see in the notes file
#space complexity: see in the notes file
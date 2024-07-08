def ssort(ar):
    N = len(ar)

    for I in range(N-1): #selected element 
        min_index = I 
        for J in range(I+1,N): #compare the selected element with next elements to find min element 
            if ar[J] < ar[min_index]:
                min_index = J
        #swap selected element and min element 
        if min_index != I:  #if selected and min elements are same, no swap [optimized]
            ar[I], ar[min_index] = ar[min_index], ar[I] # swap code 
    # the elements sorted
def solve():
    #N=len(ar)#8
    #ar = [7, 4, 3, 5, 8, 10, 2, 6]
    #ar = [3, 5, 8, 10]
    ar = [100, 88, 90, 45, 85, 67, 110, 40, 77, 92, 13, 62]
    print('Before sort:',ar)
    ssort(ar)
    print('After sort:',ar)
    
solve()

#time complexity:  see in the notes file
#space complexity: see in the notes file
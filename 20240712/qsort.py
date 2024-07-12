def partition(ar,left,right):
    pivot_index = right #pick pivot
    pivot = ar[pivot_index]
    #seek the pivot place | left..right-1
    gindex = left #greater index, new place for pivot after process
    for K in range(left,right):#scan from first to before pivot
        if ar[K] <= pivot:            
            if gindex != K:
                  ar[K], ar[gindex] = ar[gindex],ar[K] #swap greater element and less element
            gindex+=1
    #[lesser][greater][pivot] -> [lesser][pivot][greater]
    ar[gindex], ar[pivot_index] = ar[pivot_index], ar[gindex] #swap the first greater element and pivot
    #now gindex is the new place for pivot ie index of pivot
    return gindex 
def qsort(ar,left,right):
    #base condition  #  left<right - more one element, left==right - just one element, left>right - no element
    if left >= right:
        return 
    #logic
    pivot_index = partition(ar, left, right)
    qsort(ar, left, pivot_index - 1) #left list 
    qsort(ar, pivot_index + 1, right) #right list 
def solve():
    ar = [100, 88, 90, 45, 85, 67, 110, 40, 77, 92, 13, 62]
    left, right = 0, len(ar)-1
    print('Before sort:', ar)
    qsort(ar,left,right)
    print('After sort:', ar)
solve()
# time complexity: O(N log N) for best, average cases. O(N^2) for worst case.
# space complexity: O(log N) for recusion call stack memory | O(1) if not consided call stack mem
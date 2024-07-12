def merge(ar,left1,right1,right2):
    left2 = right1 + 1 
    index1, index2 = left1, left2 #index1 <- index of first list, index2 <- index of second list 
    size = right2 - left1 + 1 #size of first list + size of second list
    slist = [0 for e in range(size)] #0 filled array for the size of sorted list(slist)
    sindex = 0 #index of sorted index
    while index1 <= right1 and index2 <= right2:
        if ar[index1] < ar[index2]:
            slist[sindex] = ar[index1]
            index1 += 1
        else:
            slist[sindex] = ar[index2]
            index2 += 1
        sindex += 1    
    while index1 <= right1: #copy if elements in left list #1
        slist[sindex] = ar[index1]
        index1 += 1
        sindex += 1
    while index2 <= right2: #copy if elements in right list #2 either 1 or 2 will happen 
        slist[sindex] = ar[index2]
        index2 += 1
        sindex += 1
    #copy back from slist to actual list 
    index1 = left1    
    for sindex in range(size):
        ar[index1] = slist[sindex]
        index1+=1    

def msort(ar,left,right):
    if left>=right:
        return 
    mid = (left + right) // 2
    #1st half 
    left1, right1 = left, mid     
    msort(ar, left1, right1)
    #2nd half
    left2, right2 = mid+1, right 
    msort(ar, left2, right2) 
    #compile solution of 1st and 2nd halves
    merge(ar,left1,right1,right2)    
def solve():
    ar = [100, 88, 90, 45, 85, 67, 110, 40, 77, 92, 13, 62]
    left, right = 0, len(ar)-1
    print('Before sort:', ar)
    msort(ar,left,right)
    print('After sort:', ar)
solve()
def quickSort(aList):
    sortHelper(aList,0,len(aList)-1)
    
def sortHelper(aList,left,right):
    if left < right:
        midPoint = split(aList, left, right)
        
        sortHelper(aList,left,midPoint-1)
        sortHelper(aList,midPoint+1,right)
        
def split(aList,left,right):
    
    pivot = aList[left]
    done = False
    
    leftmark = left+1
    rightmark = right
    
    while not done:
        while leftmark <= rightmark and aList[leftmark] > pivot:
            leftmark += 1
            
        while leftmark <= rightmark and aList[rightmark] < pivot:
            rightmark -= 1
            
        if leftmark > rightmark:
            done = True
            
        elif aList[leftmark]<aList[rightmark]:
            temp = aList[leftmark]
            aList[leftmark] = aList[rightmark]
            aList[rightmark] = temp
        
    temp = aList[left]
    aList[left] = aList[rightmark]
    aList[rightmark] = temp
    
    return rightmark

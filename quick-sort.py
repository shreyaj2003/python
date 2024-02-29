unsorted1 = [65,46,54,22,69,75,43,36]

def partition (arr,start,end):
    pivot = arr[start]
    i = start
    j = end 

    while i<j:
        while arr[i]<pivot:
            i+=1
        while arr[j]>pivot:
            j-=1

        if i<j:
            arr[i],arr[j] = arr[j],arr[i]

    if j>i:
        pivot,arr[j] = arr[j],pivot

    return j 

def quicksort(arr,start,end):
    if start < end:
        index = partition(arr,start,end)
        quicksort(unsorted1,start,index-1)
        quicksort(unsorted1,index+1,end)

quicksort(unsorted1,0,len(unsorted1)-1)
print(unsorted1)
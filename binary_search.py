arr = [1,3,5,7,9,10]
item = int(input("enter the item to be searched: ")) 
lb = 0
ub = len(arr)-1
mid = int((lb+ub)/2)
while (lb <= ub and item != arr[mid]):
    if (item < arr[mid]):
        ub = mid-1
        mid = int((lb+ub)/2)
    else:
        lb = mid+1
        mid = int((lb+ub)/2)
if arr[mid] == item:
    print("item found at",mid)
else:
    print("item not found")



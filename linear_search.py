arr=[1,3,2,6,4]
item = int(input("Enter the item to search: "))
x = 0 
for i in range(len(arr)):
    if arr[i] == item:
        x=x+1
        y=i 

if x!=0:
    print("Item found at ",y)
else:
    print("match not found! ")
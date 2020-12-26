arr = [10,20,20,2,40,50,35,33,44,55,5,70]

i = 0
j = 1
while j<len(arr):
    if arr[i]<arr[j]:
        j+=1
    elif arr[i]>arr[j]:
        i=j
        j+=1
print(arr[i])
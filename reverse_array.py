def reverse_array(arr, l, r):
    if l>=r: return
    temp = arr[l]
    arr[l] = arr[r]
    arr[r] = temp
    reverse_array(arr, l+1, r-1)

l = [1,2,3,4,5,6,7,8,9,10]
reverse_array(l, 0, 9)
print(l)
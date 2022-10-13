from typing import List

def find_combination(ind, target, ans, arr, ds: List):
    if target == 0:
        ans.append(ds.copy())
        return
    if ind == len(arr):
        return
    if arr[ind] <= target:
        ds.append(arr[ind])
        find_combination(ind, target-arr[ind], ans, arr, ds)  # if you want that same index must not included then do ind + 1
        ds.pop()  # need to remove last element because after backtracking we need initial list (ds) in order to try other combinations
    
    find_combination(ind + 1, target, ans, arr, ds)
    

l = [2, 3, 4, 5, 10, 15, 20, 25, 30]
result = []
data_s = []
find_combination(0, 6, result, l, data_s)
print(result)

from typing import List

def find_subsets(ind, total, arr, n, ans: List):
    if ind == n:
        ans.append(total)
        return 
    find_subsets(ind + 1, total + arr[ind], arr, n, ans)
    find_subsets(ind + 1, total, arr, n, ans)

arr = [3, 1, 2]
initial_index = 0
initial_sum = 0
arr_len = len(arr)

subsets = []

find_subsets(initial_index, initial_sum, arr, arr_len, subsets)
print(subsets)
def find_combination(ind, arr, ans, ds, k):
    if len(ds) == k:
        if isInversed(ds):
            ans[0] += 1
        return
    if ind == len(arr):
        return
    ds.append(arr[ind])
    find_combination(ind + 1, arr, ans, ds, k)
    ds.pop()
    find_combination(ind+1, arr, ans, ds, k)

def isInversed(t):
    if t[0] > t[1] > t[2]:
        return True
    return False
def maxInversions(arr):
    data_s = []
    result = [0]
    find_combination(0, arr, result, data_s, 3)
    return result[0]
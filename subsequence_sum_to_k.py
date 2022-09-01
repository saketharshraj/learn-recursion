def find_subsequences_with_sum_k(ind, ds, arr, k, s, n):
    if ind >= n:
        if k == s:
            print(ds)
        return
    
    ds.append(arr[ind])
    s = s+arr[ind]
    find_subsequences_with_sum_k(ind+1, ds, arr, k, s, n)

    s -= ds.pop()
    find_subsequences_with_sum_k(ind+1, ds, arr, k, s, n)



l1 = [3, 1, 2]
l2 = []

find_subsequences_with_sum_k(0, l2, l1, 3, 0, len(l1))

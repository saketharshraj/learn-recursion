def subsequence(ind, ds, arr, n):
    if ind >= n:
        print(ds)
        return
    
    ds.append(arr[ind])
    subsequence(ind+1, ds, arr, n)

    ds.pop()
    subsequence(ind+1, ds, arr, n)

l1 = [3, 1, 2]
l2 = []

subsequence(0, l2, l1, len(l1))
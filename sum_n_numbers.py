def add(i, res=0):
    if i < 1:
        return res
    return add(i-1, res+i)

print(add(100))
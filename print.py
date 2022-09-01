def display(i, n, l):
    if i > n:
        return
    display(i+1, n, l)
    l.append('Hello bro !!' + str(i))
    display(i+1, n, l)
    
l = []
display(1, 10, l)
print(len(l))
def sequence_statistics():
    n = 0
    s = 0
    m = None
    print("Enter numbers one by one, end with -1:")

    while True:
        x = int(input())
        if x == -1:
            break
        n += 1
        s += x
        if m is None or x < m:
            m = x
    
    if n == 0:
        m = -1
        a = -1
    else:
        a = s / n
    
    return n, s, m, a
# it looks like I learned how to use git today

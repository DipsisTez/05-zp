for i in range(1000, 10000):
    t1, t2, t3, t4 = map(int, str(i))
    n1, n2, n3 = t1 + t2, t2 + t3, t3 + t4
    calcs = sorted([n1,n2,n3])[1:]
    if ''.join(map(str, calcs)) == '1315':
        print(i)
        

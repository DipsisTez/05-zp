#Anwser 12
k = 0

for i in range(1000, 10000):
    f = False
    t1, t2, t3,t4 = map(int, str(i))
    
    for i in [t1,t2,t3,t4]:
        if i%2==0:
            f = True
            break
    if f == True:
        continue

    n1,n2 = t1+t2, t3+t4
    calcs = sorted([n1,n2])

    if ''.join(map(str, calcs)) == '616':
        k += 1
print(k)

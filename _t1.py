#Anwser 9810

k = 0

for i in range(1000, 10000):
    t1, t2, t3,t4 = map(int, str(i))
    n1,n2 = t1+t2, t3+t4
    calcs = sorted([n1,n2])

    if ''.join(map(str, calcs)) == '117':
    	if k < i:
    		k = i
print(k)
        

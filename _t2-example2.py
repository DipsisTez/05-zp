def f(s):
	return sum(int(i) for i in s)

kR = []

for n in range(1, 100):
	s = bin(n)[2:]
	if f(s)%2==0:
		s += '10'
	else:
		s += '01'
	r = int(s, 2)
	if r<102:
		kR.append(r)

print(max(kR))
		
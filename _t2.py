def f(s):
    return sum(int(i) for i in s)

for n in range(1, 100):
    s = bin(n)[2:]  # перевод в двоичную систему
    s += str(f(s) % 2)
    s += str(f(s) % 2)
    r = int(s, 2)  # перевод в десятичную систему
    if r > 83:
        print(r)
        break

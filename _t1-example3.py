#Anwser 12
k = 0

for i in range(1000, 10000):
    digits = list(map(int, str(i)))
    
    if any(digit % 2 == 0 for digit in digits):
        continue

    sums = sorted([digits[0] + digits[1], digits[2] + digits[3]])

    if ''.join(map(str, sums)) == '616':
        k += 1

print(k)

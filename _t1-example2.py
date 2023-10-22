#anwser = 296
print(min(i for i in range(100, 1000) if ''.join(sorted([str(sum(map(int, str(i)[:2]))), str(sum(map(int, str(i)[1:])))])) == '1115'))

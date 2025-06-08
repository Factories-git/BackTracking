cnt = 0
n = int(input())
palindromes = set()
for i in ['', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
    for j in ['', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
        for k in ['', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            for r in ['', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                for c in ['', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                        s = ''.join([i, j, k, r, c]).lstrip('0')
                        if not s: continue
                        palindromes.add(int(s + s[::-1]))
                        palindromes.add(int(s + s[:-1][::-1]))

for i in palindromes:
    if i <= n:
        cnt += 1
print(cnt)
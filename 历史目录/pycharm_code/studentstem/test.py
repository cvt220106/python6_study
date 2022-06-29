s = 'hello world'
s1 = list(s[0:6])
i, j = 0, len(s1) - 1
while i < j:
    s1[i], s1[j] = s1[j], s1[i]
    i += 1
    j -= 1
print(" ".join(s1))

s = input()
count = 0

for l in s:
    if 'a' <= l <= 's':
        count += 1

if count < len(s) - count:
    print(s.upper())
else:
    print(s.lower())
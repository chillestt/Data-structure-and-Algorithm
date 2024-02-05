def word_pattern(pattern, str):
    p = list(pattern)
    s = str.split(" ")
    print(p, s)

    if len(p) != len(s):
        return False

    d = {}
    for a in range(len(p)):
        if p[a] in d:
            if d[p[a]] != s[a]:
                return False
        else:
            if s[a] in d.values():
                return False
            d[p[a]] = s[a]

    return True


pattern = "abba"
str = "dog dog dog dog"
print(word_pattern(pattern, str))

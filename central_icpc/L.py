s = "Welcome Hue University of Sciences"

def issubset(s1, s2):
    s1 = set(s1)
    s2 = set(s2)
    return s1.issubset(s2)

def L(text):
    for i in range(len(text) - 1):
        mes = text[i].strip()
        for j in range(i + 1, len(text)):
            if issubset(s, (text[j - 1] + " " + text[j])):
                return "Yes"
            mes += " " + text[j].strip()


        if issubset(s, mes):
            return "Yes"

    return "No"


lines = []

while True:
    try:
        line = input()
    except EOFError:
        break
    lines.append(line)

print(L(lines))

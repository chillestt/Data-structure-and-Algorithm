def solution(num1, num2):
    # nhan hai so binh thuong
    m, n = len(num1), len(num2)
    products = [0] * (m + n)

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            digit1 = ord(num1[i]) - ord("0")
            digit2 = ord(num2[j]) - ord("0")
            product = digit1 * digit2
            pos1, pos2 = i + j, i + j + 1
            sum_ = product + products[pos2]
            products[pos2] = sum_ % 10
            products[pos1] += sum_ // 10

    result = ""
    for digit in products:
        if result or digit != 0:
            result += str(digit)

    return result if result else "0"


print(solution("123","456"))

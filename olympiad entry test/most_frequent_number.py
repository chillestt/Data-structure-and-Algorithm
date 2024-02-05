
def mostFrequentDigit(number):
    most_frequent_digit = 0
    max_count = 0

    digit_count = [0] * 10

    while number > 0:
        digit = number % 10
        digit_count[digit] += 1
        number //= 10

        if digit_count[digit] > max_count:
            max_count = digit_count[digit]
            most_frequent_digit = digit
        elif digit_count[digit] == max_count and digit > most_frequent_digit:
            most_frequent_digit = digit

    return most_frequent_digit


a = int(input())
print(mostFrequentDigit(a))


def sum_of_digits(number):

    sum = 0
    while number > 0:
        sum += number % 10
        number //= 10
    return sum

def max_sum_of_digits(numbers):

    max_sum = 0
    max_number = None
    for number in numbers:
        sum = sum_of_digits(number)
        if sum > max_sum:
            max_sum = sum
            max_number = number
    return max_number
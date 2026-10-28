def second_lagest(numbers):
    largest =  second = None
    for number in numbers:
        if largest is None or number > largest:
            if number != largest:
                second = largest
                largest = number
        elif number != largest and (second is None or number > second):
            second = number
    return second

num = second_lagest([10, 5, 8, 10, 3])
print(num)                            
def closest_number(numbers, target):
    closest = numbers[0]
    for number in numbers:
        d1 = abs(number - target)
        d2 = abs(closest - target)
        if d1 < d2 or (d1 == d2 and number < closest):
            closest = number
        return closest
numbers = (closest_number([4, 8, 15, 20],13))
print(numbers)
           
def bigger(numbers, current_bigger = 0):
    if numbers == []:
        return current_bigger
    else:
        if numbers[0] > current_bigger:
            bigger_n = numbers[0]
        else:
            bigger_n = current_bigger
    return bigger(numbers[1:], bigger_n)

print(bigger([1,5,11,7,4,9,6]))
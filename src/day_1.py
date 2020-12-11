with open("day_1.input", "r") as reader:
    numbers = [int(line) for line in reader.readlines()]

numbers.sort()


def first_part(sorted_numbers):
    product = 0
    total = 2020
    left = 0
    right = len(sorted_numbers) - 1

    while left < right:
        current_total = sorted_numbers[left] + sorted_numbers[right]
        if current_total < total:
            left += 1
        elif current_total > total:
            right -= 1
        else:
            product = sorted_numbers[left] * sorted_numbers[right]
            break

    return product


print(first_part(numbers))


def second_part(sorted_numbers):
    product = 0

    for i in range(0, len(sorted_numbers) - 2):
        if sorted_numbers[i] > 2020:
            break
        for j in range(i + 1, len(sorted_numbers) - 1):
            if sorted_numbers[i] + sorted_numbers[j] > 2020:
                break
            for k in range(j + 1, len(sorted_numbers)):
                current_sum = sorted_numbers[i] + sorted_numbers[j] + sorted_numbers[k]
                if current_sum > 2020:
                    break
                elif current_sum == 2020:
                    product = sorted_numbers[i] * sorted_numbers[j] * sorted_numbers[k]
                    return product
    return product


print(second_part(numbers))

def sum_two_smallest_numbers(numbers):
    new_lst = [x for x in numbers if x != min(numbers)]
    result = 0
    result +=  min(numbers) + min(new_lst)
    return result
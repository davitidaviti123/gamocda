def count_positives_sum_negatives(arr):
    if arr == []:
        return []
    count = 0
    neg = 0
    for i in arr:
        if i > 0:
            count += 1
        if i < 0:
            neg += -i
    arr1 = [count, -neg]
    return arr1
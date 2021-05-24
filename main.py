def get_biggest_subarray(arr) -> list:
    subrange_start = sum_a = max_sum = max_sum_sub_start = max_sum_sub_end = 0
    arr.append(-1)  # for easy check
    for index, element in enumerate(arr):
        if element < 0:  # if negative
            if sum_a > max_sum:  # rewrite max subarray
                max_sum = sum_a
                max_sum_sub_start = subrange_start
                max_sum_sub_end = index
            sum_a = 0  # restart sum
            subrange_start = index + 1  # restart start index
        else:
            sum_a += arr[index]

    return arr[max_sum_sub_start:max_sum_sub_end]


if __name__ == '__main__':
    arr = input('Please enter your array separated by commas:')
    arr = [int(element.replace(' ', '')) for element in arr.split(',')]  # elements to int
    subarray = get_biggest_subarray(arr)
    print(subarray)

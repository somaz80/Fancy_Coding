from datetime import time
from datetime import datetime

def merge_sort(arr):
    if len(arr) > 1:
        half = len(arr) // 2
        left = arr[half:]
        right = arr[:half]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
            while i < len(left):
                arr[k] = left[i]
                i = i + 1
                k = k + 1

            while j < len(right):
                arr[k] = right[j]
                j = j + 1
                k = k + 1
        print("Merging ", arr)


def plusMinus(arr):
    positive_val = 0.000000
    negative_val = 0.000000
    zero_val = 0.000000
    len_arr = len(arr)
    for i in arr:
        if i > 0:
            positive_val = positive_val + 1.000000
        elif i < 0:
            negative_val = negative_val + 1.000000
        else:
            zero_val = zero_val + 1.000000
    print(positive_val / len_arr)
    return '{0:.6f}'.format(positive_val / len_arr), '{0:.6f}'.format(negative_val / len_arr), '{0:.6f}'.format(
        zero_val / len_arr)

# def staircase(n):
#     for i in range(n):
#         print(' ' * ((n - i)-1), '#' * i , end=' ')


def miniMaxSum(arr):

    numbers_sorted = sorted(arr)
    print(numbers_sorted)
    min_sum = 0
    max_sum = 0
    for i in range(4):
        min_sum = min_sum + numbers_sorted[i]
    print(min_sum)
    for j in range(len(numbers_sorted) - 1,len(numbers_sorted) - 4, -1):
        max_sum = max_sum + numbers_sorted[j]
    print(max_sum)

def birthdayCakeCandles(ar):
    age = len(ar)
    max_candel_length = 0
    candel_count = 0
    for i in ar:
        if i <= age:
            if i > max_candel_length:
                max_candel_length = i
                candel_count = 1
            elif i == max_candel_length:
                    candel_count = candel_count + 1
    return candel_count


def military_time(time_string):
    only_time = time_string[:-2]
    am_pm = time_string[-2:]
    time_splitted = only_time.split(':')
    
    if am_pm == 'PM' and time_splitted[0] < '12':
        time_splitted[0] = int(time_splitted[0]) + 12
    elif am_pm == 'AM' and time_splitted[0] == '12':
        time_splitted[0] = '00'

    mil_string = ''
    for i in time_splitted:
        mil_string = mil_string + str(i) + ':'
    mil_string = mil_string[:-1]

    print(mil_string)


def gradingStudents(grades):
    # Write your code here
    final_grades = []
    for i in grades:
        if i > 37:
            i = int((5 * round(i/5)) + 5)
            final_grades.append(i)
    return final_grades


def main():
    nlist = [14, 46, 43, 27, 57, 41, 45, 21, 70]
    narray = [82,49,82,82,41,82,15,63,38,25]
    # merge_sort(nlist)
    print(gradingStudents([4, 73, 67, 38, 33]))





if __name__ == '__main__':
    main()

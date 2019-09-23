import os
from os import listdir


def print_content_path(path):

    for child_dir in listdir(path):
        child_dir_path = os.path.join(path, child_dir)
        if os.path.isdir(child_dir_path):
            print_content_path(child_dir_path)
        else:
            print('Content Found : ', child_dir_path)


def print_odd_stars_diamond(user_input):
    for i in range(user_input):
        for s in range(user_input - i):
            print(' ', end='')
        for j in range((i*2) - 1):
            print(j, end='')
        print()
    for i in range(user_input, 0, -1):
        for s in range(user_input - i):
            print(' ', end='')
        for j in range((i*2) - 1):
            print(j, end='')
        print()


def print_number_pyramid_progresive(user_input):
    k = 0
    for i in range(user_input):
        for j in range(i):
            k = k + 1
            print(k, end='')
        print()


def print_number_pyramid_progresive_one(user_input):
    k = 0
    for i in range(user_input):
        for j in range(i):
            k = k + 1
            print(j+1, end='')
        print()


def print_stars_triangle_odd(user_input):
    for i in range(user_input):
        for s in range(user_input - i):
            print(' ', end='')
        for j in range((i*2) - 1):
            print('*', end='')


def print_alphabets_triangle_odd(user_input):
    '''

         A
        BCD
       EFGHI
      JKLMNOP
     QRSTUVWXY
    ZABCDEFGHIJ
   KLMNOPQRSTUVW
  XYZABCDEFGHIJKL
 MNOPQRSTUVWXYZABC

    :param user_input:
    :return:
    '''
    alphabet_start = 65
    for i in range(user_input):
        for s in range(user_input - i):
            print(' ', end='')
        for j in range((i*2) - 1):
            print(chr(alphabet_start), end='')
            alphabet_start = alphabet_start + 1
            if alphabet_start > 90:
                alphabet_start = 65
        print()


def print_alphabets_triangle_odd_rep(user_input):
    '''
    A
   BBB
  CCCCC
 DDDDDDD
    :param user_input:
    :return:
    '''
    alphabet_start = 64
    for i in range(user_input):
        for s in range(user_input - i):
            print(' ', end='')
        for j in range((i*2) - 1):
            print(chr(alphabet_start), end='')
        alphabet_start = alphabet_start + 1
        print()


def print_odd_alphabets_diamond(user_input):
    '''

    A
   BCD
  EFGHI
 JKLMNOP
ABCDEFGHI
 JKLMNOP
  QRSTU
   VWX
    Y
    :param user_input:
    :return:
    '''
    alphabet_start = 65
    for i in range(user_input):
        for s in range(user_input - i):
            print(' ', end='')
        for j in range((i*2) - 1):
            print(chr(alphabet_start), end='')
            alphabet_start = alphabet_start + 1
        print()
    alphabet_start = 65
    for i in range(user_input, 0, -1):
        for s in range(user_input - i):
            print(' ', end='')
        for j in range((i*2) - 1):
            print(chr(alphabet_start), end='')
            alphabet_start = alphabet_start + 1
        print()

def print_top_down_diamond(user_input):

    for i in range(user_input, 0, -1):
        for j in range(i):
            print('*', end='')
        print()


def print_top_down_diamond_numbers(user_input):
    number_cache = 1
    for i in range(user_input, 0, -1):
        for j in range((i * 2) - 1):
            print(number_cache, end='')
            number_cache = number_cache + 1
        print()


def print_numbers_pyramid_progressive(user_input):
    number_cache = 1
    for i in range(user_input):
        for j in range((i * 2) - 1):
            print(number_cache, end=' ')
            number_cache = number_cache + 1
        print()


def print_numbers_pyramid_progressive_right_aligned(user_input):
    num = 1
    count = 0
    decr = 8
    for i in range(0, 5):
        for k in range(0, decr):
            print(end=" ")
        for j in range(0, i):
            count = count + 1
        num = count
        temp = num
        for j in range(0, i):
            print(num, end=" ")
            num = num - 1
        print()
        num = temp
        decr = decr - 2


def reverse_words_in_string(input_string):
    '''
      Reverse each word in a given string
    :param input_string:
    :return:
    '''
    list_words = input_string.split()
    for i in range(len(list_words)):
        print(list_words[i][::-1], end=' ')


def fibonnaci(input_number):
    a = 0
    b = 1
    for i in range(input_number + 1):
        print(a)
        c = a + b
        a = b
        b = c


def fibonnaci_recur(input_number):
    if input_number <= 1:
        return input_number
    else:
        return fibonnaci_recur(input_number - 1) + fibonnaci_recur(input_number - 2)

def factor_recur(input_number):
    if input_number == 1:
        return input_number
    else:
        return input_number * factor_recur(input_number-1)


def power_get(number_input):
    number_output = 1
    for i in range(number_input+1):
        number_output = number_output * 5
    return number_output


def get_magic_number(number_input):
    print(format(5, 'b'))
    list_val = format(number_input, 'b')
    #print(len(list_val))
    length_string = len(list_val)
    magic_number = 0
    for i in range(length_string-1, -1, -1):
        if int(list_val[i]) == 1:
            magic_number = magic_number + power_get(i)
        else:
            magic_number = magic_number + 0
    print(magic_number)

def main():



if __name__ == '__main__':
    main()

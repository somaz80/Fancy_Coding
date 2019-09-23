

def reverse_string_without_special(input_string):
    forward = 0
    length = len(input_string) - 1
    list_string = string_to_list(input_string)
    print(list_string)
    while forward < length:
        if not list_string[forward].isalpha():
            forward = forward + 1
        elif not list_string[length].isalpha():
            length = length - 1
        elif list_string[length].isalpha() and list_string[forward].isalpha():
            list_string[length], list_string[forward] = list_string[forward], list_string[length]
            forward = forward + 1
            length = length - 1
    print(list_string)


def string_to_list(input_string):
    list_chars = []
    for i in input_string:
        list_chars.append(i)
    return list_chars

def main():
    reverse_string_without_special('Ab,c,de!$')
   # print_stars(8)


if __name__ == '__main__':
    main()

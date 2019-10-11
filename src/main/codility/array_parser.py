import re

#LEFT(RIGHT(CORTECHCROSSCHARGEREPORT[CostCenter],5), 5))

operations = []
inner_component = []


def get_string_inside_outermost_parentheses(text):
    content_p = re.compile(r"(?<=\().*(?=\))")
    r = content_p.search(text)
    return r.group()


# def parse_string_and_translate(string_input):
#     #print(string_input)
#
#     extracted_content = get_string_inside_outermost_parentheses(string_input)
#     print(extracted_content)
#     string_out = string_input.split('(' + extracted_content + ')')
#     print('String output', string_out)
#     operations.append(string_out)
#     print(extracted_content)
#     if '(' in extracted_content:
#         extracted_content = get_string_inside_outermost_parentheses(extracted_content)
#         string_out = string_input.split('(' + extracted_content + ')')
#         operations.append(string_out)
#         print('rest is :', operations)
#     else:
#         print(string_out)


def get_string_inside_innermost_parentheses(text):
    content = []
    while '(' in text:
        text = get_string_inside_outermost_parentheses(text)
        content.append(text)
    print(content)
    return content


def parse_string(input_string):
    temp_opt = ''
    fact_opt = []
    while '(' in input_string:
        temp_opt = get_string_inside_outermost_parentheses(input_string)
        print(temp_opt)
        operations.append(input_string.split('(' + temp_opt + ')')[0])
        print(operations)
        input_string = temp_opt


def get_inner_parameter(input_string):


    return input_string[input_string.rfind('(') + 1:input_string.find(')')].split(',')

def main():

   # print_stars(8)

    str_input = 'LEFT(RIGHT(CORTECHCROSSCHARGEREPORT[CostCenter],5), 5))'
    parse_string(str_input)
    print(operations)
    print(str_input.rfind('('))
    print(str_input.rfind(')'))
    print(str_input[str_input.rfind('(') + 1:str_input.find(')')].split(','))
    print(get_inner_parameter(str_input))
    # str_output = get_string_inside_outermost_parentheses(str_input)
    # print(str_output)
    #
    # str_output = get_string_inside_outermost_parentheses(str_output)
    #
    # print(str_output)


if __name__ == '__main__':
    main()


def solution(self, A):
    final_list = []
    for num in A:
        if num not in final_list:
            final_list.append(num)
        else:
            final_list.remove(num)
    return final_list[0]

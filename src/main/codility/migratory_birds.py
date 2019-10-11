from collections import OrderedDict
import operator


def migratory_birds(arr):
    bird_dict = {}
    for i in range(len(arr)):
        if arr[i] in bird_dict:
            bird_dict[arr[i]] += 1
        else:
            bird_dict[arr[i]] = 1
    sorted_x = sorted(bird_dict.items(), key=lambda kv: kv[1])
    print(sorted_x)
    return max(bird_dict.iteritems(), key = operator.itemgetter(1))[0]


def shoc_marchent(n, ar):
    dict_schoc = {}
    temp_eml = None
    even_soc = 0
    for i in range(n):
        temp_eml = ar[i]
        if temp_eml in dict_schoc:
            dict_schoc[temp_eml] = dict_schoc[temp_eml] + 1
        else:
            dict_schoc[temp_eml] = 1

    for key, value in dict_schoc.items():
        if value >= 2:
            even_soc += value//2
    return even_soc





def main():
    nlist = [4,5,5,5,6,6,4,1,4,4,3,6,6,3,6,1,4,5,5,5]
    print(shoc_marchent(20,nlist))


if __name__ == '__main__':
    main()




def merge_sort(arr):
    if len(arr) > 1:
        half = arr//2
        left = arr[half:]
        right = arr[:half]
        merge_sort(left)
        merge_sort(right)
        i=j=k=0

        while i < len(left) and  j < len(right):
            if left[i]  < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k +=1



def main():

   # print_stars(8)


if __name__ == '__main__':
    main()
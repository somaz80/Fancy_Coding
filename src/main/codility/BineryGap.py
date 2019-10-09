
class Solution(object):
    def __init__(self):
        self.zero_count = 0
        self.str_binary = ''

    # def binaryGap(self, N):
    #     indices = [bit for bit, x in enumerate(f'{N:0b}') if x == '1']
    #     lengths = (end - beg for beg, end in zip(indices, indices[1:]))
    #     return max(lengths, default=1) - 1

    def binaryGapOne(self, N):

        # if N > 1:
        #     self.binaryGapModified(N >> 1)
        #     print('value of N', N)
        # print(N & 1)
        print(format(N, 'b'))
        print(len(max(format(N, 'b').strip('0').split('1'))))

    def binaryGapTwo(self, N):
        print(self.get_binary_value(N))


    def get_factorial(self, n):
        i = 1
        factorial = 1
        while i <= n:
            factorial *= i
            i += 1
        print(factorial)

    def get_recur_factor(self, n):

        if n == 1:
            return n
        else:
            return n * get_recur_factor(n-1)

    def recur_get_fibo(self, n):

        if n <= 1:
            return n
        else:
            return self.recur_get_fibo(n-1) + self.recur_get_fibo(n-2)

    def solution_get(self, a):
        final_list = []

        for i in a:
            if i not in final_list:
                final_list.append(i)
        return final_list

    def remove(self, duplicate):
        final_set = set()
        unique_list = set()
        duplicate.sort()
        print(duplicate)
        for num in duplicate:
            if num not in final_set:
                final_set.add(num)
            else:
                unique_list.add(num)
        return final_set.difference(unique_list), duplicate, unique_list

    def cyclic_rotation(self, A, K):
        print(A , K)
        if len(A) == 0:
            return A
        print('Module', K % len(A))
        K = K % len(A)
        print(K)
        print(A[-K:])
        print(A[:-K])
        return A[-K:] + A[:-K]

    def whatisthis(self, n):
        print(n // 2)

    # main method for standalone run
def main():
    sol = Solution()
    arr = [3, 8, 9, 7, 6]
    counter = 3
    A = [7, 6]
    K = 1
    #print(sol.cyclic_rotation(arr, 7))
    sol.whatisthis(2)

    #number_fmt = 111510
    #print(len(max(format(number_fmt, 'b').strip('0').split('1'))))
if __name__ == '__main__':
    main()


from typing import List

def bubble_sort(num):
    for i in range(len(num)):
        for j in range(len(num) - 1 - i):
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]
    return num


if __name__ == '__main__':
    import random
    num = [10, 8, 2, 5, 7, 9]
    print(bubble_sort(num))
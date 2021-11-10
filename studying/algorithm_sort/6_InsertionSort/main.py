def insertion_sort(nums):
    for i in range(1, len(nums)):
        tmp = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > tmp:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = tmp

    return nums


if __name__ == '__main__':
    nums = [45, 61, 3, 34, 82, 41, 99]
    print(insertion_sort(nums))

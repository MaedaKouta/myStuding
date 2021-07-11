def shell_sort(nums):
    gap = len(nums) // 2
    while gap > 0:
        for i in range(gap, len(nums)):
            tmp = nums[i]
            j = i
            while j >= gap and nums[j - gap] > tmp:
                nums[j] = nums[j - gap]
                j -= gap
            nums[j] = tmp
        gap //= 2
    return nums


if __name__ == '__main__':
    nums = [54, 32, 2, 76, 39, 47, 99, 15]
    print(shell_sort(nums))

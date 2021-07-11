def comb_sort(nums):
    gap = len(nums)
    swap = True

    # gapが1で、かつ入れ替えが行われなくなるまでループを行う
    while gap != 1 or swap:
        gap = int(gap / 1.3)
        if gap < 1:
            gap = 1
        swap = False

        for i in range(0, len(nums) - gap):
            if nums[i] > nums[i + gap]:
                nums[i], nums[i + gap] = nums[i + gap], nums[i]
                swap = True
    return nums


if __name__ == '__main__':
    nums = [20, 54, 94, 5, 35, 61, 49, 44]
    print(comb_sort(nums))

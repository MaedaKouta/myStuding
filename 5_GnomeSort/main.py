def gnome_sort(nums):
    value = 0
    while value < len(nums):
        if value == 0:
            value += 1
        if nums[value] >= nums[value - 1]:
            value += 1
        else:
            nums[value], nums[value - 1] = nums[value - 1], nums[value]
            value -= 1
    return nums

if __name__ == '__main__':
    nums = [43, 56, 55, 12, 68, 87, 17, 11]
    print(gnome_sort(nums))

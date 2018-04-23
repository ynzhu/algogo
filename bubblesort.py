import random
def getrandata(num):
    nums = []
    for i in range(num):
        nums.append(random.randint(0,100))
    return nums

def bubblesort(nums):
    if len(nums) <= 1:
        return nums
    for num1 in range(len(nums)-1):
        for num2 in range(num1+1, len(nums)):
            if nums[num1] > nums[num2]:
                nums[num1], nums[num2] = nums[num2], nums[num1]
    return nums

def main():
    nums = getrandata(10)
    print nums
    print bubblesort(nums)

main()
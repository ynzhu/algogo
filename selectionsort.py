import random
def getrandata(num):
    nums = []
    for i in range(num):
        nums.append(random.randint(1,100))
    return nums

def selectionSort(nums):
    for i in range(len(nums)-1):
        temp = nums[i]
        swapindex = -1
        for j in range(i+1, len(nums)):
            if nums[j] < temp:
                temp = nums[j]
                swapindex = j
        nums[i], nums[swapindex] = temp, nums[i]
    return nums

def main():
    nums = getrandata(10)
    print nums
    print selectionSort(nums)

main()
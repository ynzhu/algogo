import random
def getrandata(num):
    nums = []
    for i in range(num):
        nums.append(random.randint(1,100))
    return nums

def insertSort(nums):
    for j in range(len(nums)):
        for i in range(j,0,-1):
            if nums[i] < nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
            else:
                break
    return nums

def main():
    nums = getrandata(10)
    print nums
    print insertSort(nums)
main()
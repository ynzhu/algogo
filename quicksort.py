import random
def getrandata(num):
    nums = []
    for i in range(num):
        nums.append(random.randint(0,100))
    return nums

def quicksort(nums):
    if len(nums) <= 1:
        return nums
    less = []
    greater = []
    base = nums.pop()
    for n in nums:
        if n < base:
            less.append(n)
        else:
            greater.append(n)
    return quicksort(less) + [base] + quicksort(greater)

def main():
    nums = getrandata(10)
    print nums
    print quicksort(nums)

main()
def dfs(nums, l, total, target):
    res = 0
    if l == len(nums):
        if total == target:
            return 1
        else:
            return 0
    else:
        res += dfs(nums, l+1, total+nums[l], target)
        res += dfs(nums, l+1, total-nums[l], target)
        return res

def solution(numbers, target):
    return dfs(numbers, 0, 0, target)
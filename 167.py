class Solution:
    def twosum(self,numbers,target):
        """输入有序数组"""
        left = 0    # 左指针
        right = len(numbers) - 1    # 右指针
        while True:
            s = numbers[left] + numbers[right]
            if s == target: #判断和与target的大小
                break
            if s > target:  # 和偏大，右侧往左移
                right -= 1
            else:
                left += 1   # 和偏小，左侧往右移
        return [left+1, right+1]    # 题目要求下标从1开始

# 时间复杂度 O(n)
# 空间复杂度 O(1)
solution = Solution()
test1 = [2,7,11,15]
target1 = 9
result1 = solution.twosum(test1,target1)
print("示例1的结果为: ",result1)

test2 = [2,3,4]
target2 = 6
result2 = solution.twosum(test2, target2)
print("示例2的结果为: ",result2)

test3 = [-1, 0]
target3 = -1
result3 = solution.twosum(test3, target3)
print("示例3的结果为: ",result3)
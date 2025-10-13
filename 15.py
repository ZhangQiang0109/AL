class Solution:
    def threeSum(self,nums):
        """
        三数之和
        """
        # 先对数组进行排序，变成有序的
        nums.sort() # sort方法的()不要忘记了！  O(nlogn)

        # 列表长度
        n = len(nums)
        # 初始化答案列表
        ans = []

        # 遍历列表
        for i in range(n-2):    #   O(n)
            j = i + 1   # j是右侧一个
            k = n - 1   # k是最大一个

            if i > 0 and nums[i] == nums[i-1]:  # 去掉重复的三元组
                continue    # 进入下一轮循环(跳过当前i，进入下一个i)
            # if nums[i] + nums[i+1] + nums[i+2] > 0:     # 与后面紧挨最小两数相加
            #     break       # 终止整个循环
            # if nums[i] + nums[n-1] + nums[n-2] < 0 :    # 与后面最大两数相加
            #     continue    # 有机会，换下一个i

            while j < k:    # 双指针 O(n)
                s = nums[i] + nums[j] + nums[k]
                if s > 0:
                    k -= 1
                elif s < 0:
                    j += 1
                else:   # s == 0 
                    ans.append([nums[i],nums[j],nums[k]])   #这里是添加三元组，注意[]
                    j += 1  # 左指针 向右走一步
                    k -= 1  # 右指针 向左走一步
                    while j < k and nums[j] == nums[j-1]:   # 跳过重复数字（左）
                        j += 1  # 在向右走一步
                    while k > j and nums[k] == nums[k+1]:   # 跳过重复数字（右）
                        k -= 1
        return ans

# 时间复杂度 O(n^2)     O(n^2)>O(nlogn)
# 空间复杂度 O(1)

solution = Solution()
test1 = [-1,0,1,2,-1,-4]
result1 = solution.threeSum(test1)
print("示例1的结果: ",result1)

test2 = [0,1,1]
result2 = solution.threeSum(test2)
print("示例2的结果: ",result2)

test3 = [0,0,0]
result3 = solution.threeSum(test3)
print("示例3的结果: ",result3)
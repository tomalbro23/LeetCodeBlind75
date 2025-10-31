class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        seen = dict()
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

def main():
    solution = Solution()
    print("Solution: [0,1]\nAnswer: ",solution.twoSum([2, 7, 11, 15], 9))
    print("Solution: [1,2]\nAnswer: ",solution.twoSum([3, 2, 4], 6))
    print("Solution: [0,1]\nAnswer: ",solution.twoSum([3, 3], 6))

if __name__ == "__main__":
    main()
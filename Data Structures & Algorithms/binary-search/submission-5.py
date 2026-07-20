class Solution:
    def search(self, nums: List[int], target: int) -> int:
        baixo = 0
        alto = len(nums) - 1

        while baixo <= alto:
            meio = (baixo + alto) // 2
            chute = nums[meio]
            if chute == target:
                return meio
            if chute > target:
                alto = meio - 1
            else:
                baixo = meio + 1
        
        return -1
        
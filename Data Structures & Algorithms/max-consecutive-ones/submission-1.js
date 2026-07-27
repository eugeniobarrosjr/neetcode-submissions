class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findMaxConsecutiveOnes(nums) {
        let max = 0
        let current = 0

        for (const num of nums) {
            current = num === 1 ? current + 1 : 0
            max = Math.max(current, max)
        }

        return max
    }
}

from heapq import heapify, heappop, heappush


class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        # Create a priority queue with (value, index)
        pq = [(val, i) for i, val in enumerate(nums)]
        heapify(pq)  # Min-heap

        for _ in range(k):
            _, i = heappop(pq)  # Pop the smallest element
            nums[i] *= multiplier  # Multiply it by the multiplier
            heappush(pq, (nums[i], i))  # Push the updated value back into the heap

        return nums


# User input
input_str = input("Enter the numbers (comma-separated): ")
nums = list(map(int, input_str.split(',')))
k = int(input("Enter the number of operations (k): "))
multiplier = int(input("Enter the multiplier: "))

# Compute final state
solution = Solution()
final_state = solution.getFinalState(nums, k, multiplier)

print("Final state of the list:", final_state)
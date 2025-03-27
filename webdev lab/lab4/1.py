class Subsets:
    def __init__(self, nums):
        self.nums = nums

    def generate_subsets(self):
        result = []
        self._backtrack(sorted(self.nums), 0, [], result)
        return result

    def _backtrack(self, nums, start, path, result):
        result.append(path)
        for i in range(start, len(nums)):
            self._backtrack(nums, i + 1, path + [nums[i]], result)

# Taking user input
user_input = input("Enter numbers separated by spaces: ")
nums = list(map(int, user_input.split()))  # Convert input into a list of integers

# Generate subsets
subsets = Subsets(nums)
print(subsets.generate_subsets())


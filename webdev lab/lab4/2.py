class PairFinder:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def find_pair(self):
        num_to_index = {}
        for index, num in enumerate(self.nums):
            complement = self.target - num
            if complement in num_to_index:
                return (num_to_index[complement], index, complement, num)
            num_to_index[num] = index
        return None

# Example usage:
user_input = input("Enter numbers separated by spaces: ")
nums = list(map(int, user_input.split()))
target = 9
pair_finder = PairFinder(nums, target)
result = pair_finder.find_pair()
if result:
    index1, index2, num1, num2 = result
    print(f"Pair found at indices: {index1} and {index2}")
    print(f"Numbers: {num1} and {num2}")
else:
    print("No pair found.")

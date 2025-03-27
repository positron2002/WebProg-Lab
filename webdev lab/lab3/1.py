import math

# Function to calculate mean
def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

# Function to calculate variance
def calculate_variance(numbers, mean):
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)

# Function to calculate standard deviation
def calculate_std_deviation(variance):
    return math.sqrt(variance)

# Read N numbers from the console
N = int(input("Enter the number of elements: "))
numbers = []
for _ in range(N):
    number = float(input("Enter a number: "))
    numbers.append(number)

# Calculate mean, variance, and standard deviation
mean = calculate_mean(numbers)
variance = calculate_variance(numbers, mean)
std_deviation = calculate_std_deviation(variance)

# Print the results with suitable messages
print(f"Mean: {mean}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_deviation}")

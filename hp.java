def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    
    # Bug: Division by zero if the list is empty
    return total / len(numbers)

# Bug: Modifying a list while iterating over it
data = [10, 20, 30, 40, 50]
for item in data:
    if item > 20:
        data.remove(item)

print("Remaining data:", data)
print("Average:", calculate_average(data))

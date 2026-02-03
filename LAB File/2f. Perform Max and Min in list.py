data = [12, 45, 7, 89, 23]

print("Maximum:", max(data))
print("Minimum:", min(data))

# Alternative approach without using built-in functions
numbers = [12, 45, 7, 89, 23]

maximum = numbers[0]
minimum = numbers[0]

for i in numbers:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i

print("Maximum =", maximum)
print("Minimum =", minimum)

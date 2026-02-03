numbers = [10, 20, 30, 40, 50]

n = len(numbers)


total = 0
for i in numbers:
    total = total + i
mean = total / n

numbers.sort()

if n % 2 == 0:
    median = (numbers[n//2 - 1] + numbers[n//2]) / 2
else:
    median = numbers[n//2]

sum_sq = 0
for i in numbers:
    sum_sq = sum_sq + (i - mean) ** 2

variance = sum_sq / n
sd = variance ** 0.5

print("Mean =", mean)
print("Median =", median)
print("Standard Deviation =", sd)

list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = list1 + list2
print("Concatenation:", result)

add_list = []
for i in range(len(list1)):
    add_list.append(list1[i] + list2[i])

print("Element-wise Addition:", add_list)

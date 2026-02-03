str = "My name is Shashwat"

l1 = str.split()   

l2 = []

max_str = ""

for i in range(len(l1)):
    l2.append((l1[i], len(l1[i])))
    
for item in l2:
    if item[1] > len(max_str):
        max_str = item[0]
    
print(f"Longest word: {max_str} with length {len(max_str)}")
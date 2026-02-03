str = input("Enter a string: ")
charcount = {}
for char in str:
    if char in charcount:
        charcount[char] += 1
    else:
        charcount[char] = 1
for char in str:
    if charcount[char] == 1:
        print(f"First non-repeating character: {char}")
        break
else:
    print("No non-repeating character found")

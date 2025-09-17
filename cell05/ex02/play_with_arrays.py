Original_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 11, 11, 12]
New_array = [x + 2 for x in Original_array if x > 5]

print("Original array:", Original_array)
print("New array:", New_array)
hat_list = [1, 2, 3, 4, 5]  # Starting list

# Step 1: Prompt the user to replace the middle number (index 2)
hat_list[2] = int(input("Enter an integer to replace the middle number: "))

# Step 2: Remove the last element from the list
del hat_list[-1]  # or hat_listpop()

# Step 3: Print the length of the existing list
print(len(hat_list))

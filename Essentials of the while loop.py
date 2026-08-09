blocks = int(input())

height = 0
used = 0
layer = 1

while used + layer <= blocks:
    used += layer
    height += 1
    layer += 1

print("The height of the pyramid:", height)

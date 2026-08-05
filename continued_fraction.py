# Task: Evaluate a continued (nested) fraction expression:
# y = 1 / (x + 1 / (x + 1 / (x + 1 / x)))

x = float(input("Enter value for x: "))

y = 1 / (x + 1 / (x + 1 / (x + 1 / x)))

print("y =", y)

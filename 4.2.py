s = input()
alpha_count = 0
digit_count = 0
for char in s:
    if char.isalpha():
        alpha_count += 1
    elif char.isdigit():
        digit_count += 1
print(alpha_count)
print(digit_count)

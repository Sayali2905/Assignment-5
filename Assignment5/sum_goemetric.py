n = int(input("Enter number of terms: "))

sum = 0
term = 1

for i in range(1, n + 1):
    sum = sum + term
    term = term * 2

print(f"Sum of series = {sum}")
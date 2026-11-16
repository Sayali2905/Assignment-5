start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for num in range(start, end + 1):
    temp = num
    t = num
    sum = 0
    digits = 0

    while (t > 0):
        digits = digits + 1
        t = t // 10

    while (temp > 0):
        rem = temp % 10
        sum = sum + rem ** digits
        temp = temp // 10

    if (sum == num):
        print(num, end=" ")
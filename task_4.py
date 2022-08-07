a = int(input("Введите число: "))
b = 0
while a > 1:
    if b < a % 10:
        b = a % 10
    a = a // 10
print(f"Самая большая цифра в числе: {b}")


integer = int(raw_input("Enter a ten-digit number please: "))

zero_count = 0
even_count = 0
odd_count = 0

def digit_count(x):
    while x > 0:
        if x % 10 == 0:
            zero_count += 1
        elif x % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        x / 10

    print(zero_count)
    print(even_count)
    print(odd_count)




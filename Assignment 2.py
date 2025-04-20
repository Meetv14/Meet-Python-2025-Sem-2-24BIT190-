# Name : Meet Vaswani
# ROLL NO. : 24BIT190

# 1. Largest and smallest out of two
def largest_and_smallest(a, b):
    print("Name : MEET VASWANI\nROLL NO. : 24BIT190")
    if a > b:
        print(f"Largest: {a}")
        print(f"Smallest: {b}")
    elif b > a:
        print(f"Largest: {b}")
        print(f"Smallest: {a}")
    else:
        print("Both numbers are equal.")

# 2. Largest and smallest out of three
def largest_and_smallest_three(a, b, c):
    print("Name : MEET VASWANI\nROLL NO. : 24BIT190")
    if a >= b and a >= c:
        largest = a
    elif b >= a and b >= c:
        largest = b
    else:
        largest = c

    if a <= b and a <= c:
        smallest = a
    elif b <= a and b <= c:
        smallest = b
    else:
        smallest = c

    print(f"Largest: {largest}")
    print(f"Smallest: {smallest}")

# 3. Odd or Even
def odd_or_even(n):
    print("Name : MEET VASWANI\nROLL NO. : 24BIT190")
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

# 4. Divisible by 10
def divisible_by_10(n):
    print("Name : MEET VASWANI\nROLL NO. : 24BIT190")
    if n % 10 == 0:
        print("Divisible by 10")
    else:
        print("Not divisible by 10")

# 5. Minor or Major
def check_age(age):
    print("Name : MEET VASWANI\nROLL NO. : 24BIT190")
    if age < 18:
        print("Minor")
    else:
        print("Major")

# 6. Number of digits
def count_digits(n):
    print("Name : MEET VASWANI\nROLL NO. : 24BIT190")
    count = len(str(abs(n)))
    print(f"Number of digits: {count}")

# 7. Leap year check
def is_leap_year(year):
    print("Name : MEET VASWANI\nROLL NO. : 24BIT190")
    if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        print("Leap Year")
    else:
        print("Not a Leap Year")

# 8. Valid triangle
def is_valid_triangle(a1, a2, a3):
    print("Name : MEET VASWANI\nROLL NO. : 24BIT190")
    if a1 + a2 + a3 == 180:
        print("Valid Triangle")
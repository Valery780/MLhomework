#1
import math
def main():
    while True:
        x = float(input("Введите число: "))
        if x >= 0:
            sq_root = math.sqrt(x)
            print("Квадратный корень: " + str(sq_root))
        else:
            break
if __name__ == '__main__':
    main()
    
 #2
def max_digital():
    n = int(input("Enter N: "))
    nums = [input("Enter numbers: ") for _ in range(n)]
    return max(nums)
print("Max number " + max_digital())

#4
def fibonacci(a):
    ovalue = 0
    value = 1
    if a < 1:
        return 0
    for _ in range(a):
        hold = value
        value += ovalue
        ovalue = hold
    return value

print(1, *(fibonacci(a) for a in range(1, int(input("N: ")))))

#5
def fib(n):
    a = int(input("N:" ))
    if n < 1:
        return 0
    for n in range(a):
        return fib(n) < a
    print((fib(n)) for n in range(a))

# №1
while True:
    name = input("Enter name: ")
    if name.isalpha():
        break
    print("Please enter characters A-Z only")

print('Hello,',name+'!')

# №2
def main():
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    d = sum([a, b, c])
    assert d == sum([a, b, c])
    print("Sum = " + str(d))

if __name__ == '__main__':
    main()
print("Everything passed")

# №3
def main():
    num = int(input("Enter a number: "))
    print('The next number: ' + str(num + 1))
    print('The previous number: ' + str(num - 1))
if __name__ == '__main__':
    main()
print("Everything passed")

# №4
area = int(input('Enter a square area: '))
def sq_side():
    side = str(area ** 0.5)
    print("Square side: " + side)
if __name__ == '__main__':
    sq_side()
    
# №5
a = int(input())
b = int(input())
c = int(input())
p = (a + b + c) / 2
def area():
    import math
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return area
print('The triangle area: ' + str(area()))

if __name__ == '__main__':
    area()
    
# №6
amount = int(input("Введите сумму: "))
percent = int(input("ведите процент: "))
def credit():
    if amount > 0 and percent > 0:
        overpay = (amount * (percent/100))
        total = (amount * ((100 + percent)/100))

        print("Общая сумма: " + str(total))
        print("Переплата: " + str(overpay))
    else:
        print("Ошибка")
if __name__ == '__main__':
    credit()

# №7 (№11)(changed)
def calculator():
    while True:
        x = float(input("x = "))
        y = float(input("y = "))
        if x >= 0 and y != 0:
            print('%.2f + %.2f = %.2f' % (x, y, x+y))
            print('%.2f - %.2f = %.2f' % (x, y, x-y))
            print('%.2f * %.2f = %.2f' % (x, y, x*y))
            print('%.2f / %.2f = %.2f' % (x, y, x/y))
        elif x <= 0 and y != 0:
            print('%.2f + %.2f = %.2f' % (x, y, x + y))
            print('%.2f - %.2f = %.2f' % (x, y, x - y))
            print('%.2f * %.2f = %.2f' % (x, y, x * y))
            print('%.2f / %.2f = %.2f' % (x, y, x / y))
        else:
            print("Деление на ноль!")

if __name__ == '__main__':
    calculator()
# №8
import random
from random import randint

def main():
    x = int(input())
    y = int(input())

    a = randint(x, y)
    b = random.uniform(x, y)

    print("Вывод случайного целого числа ", a)
    print("Вывод случайного рационального числа ", b)
if __name__ == '__main__':
    main()
    
# №9
def number():
    a = int(input())
    b = int(input())
    if a < b:
        print("Меньшее число:" + str(a))
    elif a == b:
        print("Одинаковые числа")
    else:
        print(b)

if __name__ == '__main__':
    number()
    
# №10
def function():
    x = int(input())
    if x > 0:
        print(1)
    elif x == 0:
        print(0)
    else:
        print(-1)

if __name__ == '__main__':
    function()
    
# №12
def main():
    a = input('a: ')
    b = input('b: ')
    c = input('c: ')
    a = float(a)
    b = float(b)
    c = float(c)
    d = b**2 - 4*a*c
    print('D = ' + str(d))
    if d < 0:
        print('Корней нет')
    elif d == 0:
        x = -b / (2 * a)
        print('x = ' + str(x))
    else:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        print('x1 = ' + str(x1))
        print('x2 = ' + str(x2))
if __name__ == '__main__':
    main()
    
# №13(changed)
def mob_rate():
    a = input('Количество минут: ')
    b = input('Количество смс: ')
    a = float(a)
    b = float(b)

    if a > 0 and a <= 100 and b > 0 and b <= 30:
        c = a * 0.3
        d = b * 0.25
        print("Стоимость тарифа: " + str(c + d) + "(грн)")
    elif a > 0 and a > 100 and b > 0 and b > 30:
        c = a * 0.3
        d = b * 0.25
        e = (c + d) - 37.5
        print("Стоимость тарифа: " + str(c + d) + "(грн)")
        print("Разница: " + str(e) + "(грн)")
    else:
        c = a * 0.3
        d = b * 0.25
        print("Стоимость тарифа: " + str(c + d) + "(грн)")
        # if a > 100 or b > 30

if __name__ == '__main__':
    mob_rate()

    
# №14(changed)
def letter():
    x = input('Введите букву: ')

    if x in 'aieouy':
        print("Это гласная буква")
    elif x in 'AIEOUY':
        print("Это гласная буква")
    else:
        print("Это согласная буква")
if __name__ == '__main__':
    letter()
    
 # №15 (changed)
def triangle():
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))

    if a + b <= c or a + c <= b or b + c <= a:
        print("Треугольник не существует")
    elif a != b and a != c and b != c:
        print("Разносторонний")
    elif a == b == c:
        print("Равносторонний")
    else:
        print("Равнобедренный")
if __name__ == '__main__':
    triangle()
    
    

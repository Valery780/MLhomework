#1
def sum_columns(array_list):
    M = len(array_list)
    N = len(array_list[0])
    result = [0 for a in range(N)]
    for a in range(M):
        for b in range(N):
            result[b] += array_list[a][b]
    return result

#2
import numpy as np
def unit_matrix():
    N = int(input("Enter a number: "))
    x = np.eye(N)
    return(x)
print(unit_matrix())

#3
import numpy as np
def transpose_matrix():
    N = int(input("Enter N: "))
    M = int(input("Enter M: "))
    a = np.random.random((N, M))
    print(a)
    a_t = a.transpose()
    return (a_t)
print("Transposed: " + str(transpose_matrix()))

#4
def word_count():
    array = ["Apple", "Tomato", "Orange", "Apple", "Apple", "Orange"]

    array_d = {}.fromkeys(array, 0)
    for a in array:
        array_d[a] += 1
    return(array_d)
print(word_count())

#5
list_inp = [80, 45, 100, 130, 25, 12, 45, 25]

def unique_elements():
    set_res = set(list_inp)
    print("The unique elements:")
    list_res = (list(set_res))

    for item in list_res:
        print(item)

if __name__ == '__main__':
    unique_elements()
    
#6
def repeated_elements():
    numbers = [int(s) for s in input("Введите ряд чисел: ").split()]
    occur_before = set()
    for num in numbers:
        if num in occur_before:
            print('Повторяется')
        else:
            print('Не повторяется')
            occur_before.add(num)
if __name__ == '__main__':
    repeated_elements()

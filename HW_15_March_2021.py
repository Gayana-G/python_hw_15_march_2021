#1
L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(L)
L.remove(L[5])
L.remove(L[4])
L.remove(L[0])
print(f'List after removing 0th, 4th, and 5th elements {L}')
print('*****************************')
#2
L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f'Printed list except the first 5 elements {L[5:]}')
print('*****************************')
#3
a = 15
b = 6
print(f'Sum of 15 and 6 is {a + b}')
print(f'Absolute number of substruction of those numbers is {abs(a - b)}')
print(f'Multiplication of those numbers is {a * b}')
print(f'Division of those numbers is {a / b}')
print('*****************************')
#4
a = '15'
b = 5
print(f'Multiplication of string and integer looks like this: {a * b}')
print(f'The result of multiplication of those numbers is {int(a) * b}')
print('If we need to print out "a + some words + b", we need to use b as a string.\n')
print((str(a) + ' is three times greater than ' + str(b)) * 10)
print('*****************************')
#5
num = [23, 568, -345, 0, 456, 3, -1]
print(f'Maximum number in this list is {max(num)}')
print(f'Minimum number in this list is {min(num)}')
print('*****************************')
#6
list = ['b', 'n', 'A', 'g', 'S', 'p', 'm' 'r', 'R', 'X', 'x', 'B' 'I', 'H', 'A', 'e', 't', 'k', 'k', 'k', '1', 'c', 'g', 'S', 'P', 'q', 'Y', 'Q']
list.sort(reverse=True)
print(list)

print('*****************************')

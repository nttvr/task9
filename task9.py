#1 блок
x=38
print('начало работы кода')
if x<0:
    print('меньше нуля')
print('конец кода')
print('')
#2 блок
a, b = 10,5
if a>b:
    print('a>b')
if a>b and a>0:
    print('успех')
if (a>b) and (a>0 or b<1000):
    print('успех')
if 5<b and b<10:
    print('успех')
print('')
#3 блок (можно сравнивать числа, строки, списки...)
if '34' > '123':
    print('успех')
if '123' > '12':
    print('успех')
if [1,2]>[1,1]:
    print('успех')
print('')
#4 блок (нельзая сравнивать ранзые типы)
#if '6' > 5:
#    print('успех')
#if [5,6] > 5:
#    print('успех')
#но
if '6' != 5:
    print('успех')
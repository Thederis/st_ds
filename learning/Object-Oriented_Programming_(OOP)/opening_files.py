import os

print(os.getcwd(), '\n')

print('1-------------\n')

print(os.listdir(), '\n')

print('2-------------\n')

print('Здесь происходит создание и запись файла\n ')
f = open('learning/Object-Oriented_Programming_(OOP)/archive/test.txt', 'w', encoding='utf8')
f.write("This is a test string\n")
f.close()

print('3-------------\n')

f = open('learning/Object-Oriented_Programming_(OOP)/archive/test.txt', 'r', encoding='utf8')
print(f.read())# не работает при f.open(..., 'w',...)
f.close()

print('4-------------\n')

print('Здесь происходит дозапись файла\n ')
f = open('learning/Object-Oriented_Programming_(OOP)/archive/test.txt', 'a', encoding='utf8')
sequence = ["other string\n", "123\n", "test test\n"]
f.writelines(sequence)
f.close()

print('5-------------\n')

f = open('learning/Object-Oriented_Programming_(OOP)/archive/test.txt', 'r', encoding='utf8')
print(f.read())# не работает при f.open(..., 'w',...)
f.close()

print('6-------------\n')

print('Задание 7.4\n')

with open('learning/Object-Oriented_Programming_(OOP)/archive/test.txt') as f:
    u = open('learning/Object-Oriented_Programming_(OOP)/archive/output.txt', 'w', encoding='utf8')
    for line in f:
        u.write(line)
    u = open('learning/Object-Oriented_Programming_(OOP)/archive/output.txt', 'r', encoding='utf8')
    print(u.read())

print('7-------------\n')

print('Задание 7.5\n')
'''
Дан файл numbers.txt, компоненты которого являются действительными числами (файл создайте самостоятельно и заполните любыми числам, в одной строке одно число). Найдите сумму наибольшего и наименьшего из значений и запишите результат в файл output.txt.
'''
with open('learning/Object-Oriented_Programming_(OOP)/archive/numbers.txt', 'w', encoding='utf8') as f:
    f.writelines(['6570\n', '21300\n', '17408\n'])

with open('learning/Object-Oriented_Programming_(OOP)/archive/numbers.txt', 'r', encoding='utf8') as f:
    
    count_list = []
    for line in f:
        num_str = line.replace('\n', '')
        list_str = list(num_str)
        output = sum(eval(x) for x in list_str)
        count_list.append(output)
    num_max = max(count_list)
    num_min = min(count_list)
    
    with open('learning/Object-Oriented_Programming_(OOP)/archive/output.txt', 'w', encoding='utf8') as output:
        output.writelines([f'Max number is {num_max}\n', f'Min number is {num_min}\n'])
        
with open('learning/Object-Oriented_Programming_(OOP)/archive/output.txt', 'r', encoding='utf8') as output:
    print(output.read())
    
'''
Решение Skillfactory:

filename = 'numbers.txt'
output = 'output.txt'

with open(filename) as f:
    min_ = max_ = float(f.readline())  # считали первое число
    for line in f:
        num =  float(line)
        if num > max_:
            max_ = num
        elif num < min_:
            min_ = num

    sum_ = min_ + max_

with open(output, 'w') as f:
    f.write(str(sum_))
    f.write('\n')
    '''
    
print('8-------------\n')

print('Задание 7.6\n')

'''В текстовый файл построчно записаны фамилии и имена учащихся класса и их оценки за контрольную. Подсчитайте количество учащихся, чья оценка меньше 3 баллов. Cодержание файла:
    
Иванов О. 4
Петров И. 3
Дмитриев Н. 2
Смирнова О. 4
Керченских В. 5
Котов Д. 2
Бирюкова Н. 1
Данилов П. 3
Аранских В. 5
Лемонов Ю. 2
Олегова К. 4
    '''
with open('learning/Object-Oriented_Programming_(OOP)/archive/text_file.txt', 'w', encoding='utf8') as f:
    f.writelines(['Иванов О. 4\n', 'Петров И. 3\n', 'Дмитриев Н. 2\n', 'Смирнова О. 4\n', 'Керченских В. 5\n', 'Котов Д. 2\n', 'Бирюкова Н. 1\n', 'Данилов П. 3\n', 'Аранских В. 5\n', 'Лемонов Ю. 2\n', 'Олегова К. 4\n'])
    
with open('learning/Object-Oriented_Programming_(OOP)/archive/text_file.txt', 'r', encoding='utf8') as f:
    
    count = 0
    for pupil in f:
        if eval(pupil[-2]) < 3:
            count += 1
    print(count, '\n')
    
'''
Решение Skillfactory:
    
count = 0
for line in open("input.txt"):
    points = int(line.split()[-1])
    if points < 3:
        count += 1
        '''
    
print('9-------------\n')

print('Задание 7.7\n')

'''Выполните реверсирование строк файла (перестановку строк файла в обратном порядке).'''

with open('learning/Object-Oriented_Programming_(OOP)/archive/text_file.txt', 'r', encoding='utf8') as f:
    
    with open('learning/Object-Oriented_Programming_(OOP)/archive/text_file_revers.txt', 'w', encoding='utf8') as revers:
        for line in f.readlines()[::-1]:
            revers.write(line)

with open('learning/Object-Oriented_Programming_(OOP)/archive/text_file_revers.txt', 'r', encoding='utf8') as f:
    print(f.read())
    
'''
Решение Skillfactory:
    
with open("input.txt", "r") as input_file:
    with open("output.txt", "w") as output_file:
        for line in reversed(input_file.readlines()):
            output_file.write(line)
            '''
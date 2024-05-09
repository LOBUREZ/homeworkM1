def print_params(a=5, b='sting', c=True):  # голова функции
    print(a, b, c)
#print_params(1, 'ad', 'istina', 25) # не должно быть < или >,чем в голове функции

print_params()  # вызов функции без аргументов
print_params(b = 25)  # вызов функции с заменой 2го элемента, именной параметр
print_params(c=[1, 2, 3])  # вызов функции с заменой 3го элемента

values_list = [1, 'ton', 2.5]
values_dict = {'a': 888, 'b': 777, 'c': 666}
print_params(*values_list)  # подставилось верно т.к. 3 параметра и 3 аргумента
print_params(**values_dict)  # подставилось верно т.к. 3 параметра и 3 аргумента

values_list_2 = [True, 'Dubstep']
print_params(*values_list_2, 42) # я понял что тут переворачивает и как бы заменяет аргументы, т.е.
# True - это а, 'Dubstep' - это b, с - это 42

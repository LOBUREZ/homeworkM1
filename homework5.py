my_list = ['apple', 'banana', 'peach', 'grape', 'coconut', 'orange']  # список
print(my_list)
#print(my_list[::-1])  я не могу понять, как в 1ой строке вывести 1ое и последнее значение
print(my_list[0])  # 1ый элемент
print(my_list[-1])  # последний эелемент
print(my_list[2:5])  # срез с 3го по 4ый элемент, 5ый элемент не вклюючен
my_list[2] = 'lemon'  # замена 3го элемента
print(my_list)
my_dict = {'apple': 'яблоко', 'banana': 'банан', 'peach': 'персик', 'grape': 'грейпфрут', 'coconut': 'кокос',
           'orange': 'апельсин'}  # словарь
print(my_dict['peach'])  # вывод отдельного ключа
my_dict['banana'] = 'не банан'  # замена значения ключа
print(my_dict)

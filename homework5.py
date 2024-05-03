my_list=['apple', 'banana', 'peach', 'grape', 'coconut', 'orange']          #список
print(my_list)
print(my_list[0:6:5]) #тут просто вывел на одной строке
print(my_list[0]) # 1ый элемент
print(my_list[5]) # последний эелемент
print(my_list[2:]) # срез с 3го по 6ый элемент
my_list[2]='lemon'       #замена 3го элемента
print(my_list)

my_dict={'apple': 'яблоко', 'banana': 'банан', 'peach': 'персик', 'grape': 'грейпфрут', 'coconut': 'кокос', 'orange': 'апельсин'}   #словарь
print(my_dict['peach'])     #вывод отдельного ключа
my_dict['banana']='не банан'   # замена значения ключа
print(my_dict)
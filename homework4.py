immutable_var='banana', 'bgg', 1, 5, True
print(immutable_var)
#immutable_var[1]='egg'
#тип кортежа не поддерживает изменений эелемента
mutable_list=['pig','chicken','dog', 'cat']
print(mutable_list)
mutable_list.remove('chicken')
mutable_list.append('coow')
print(mutable_list)
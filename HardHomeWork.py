grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
list_stud = sorted(list(students))
dict_stud = {}
z_1 = (sum(grades[0])/(len(grades[0])))
z_2 = (sum(grades[1])/(len(grades[1])))
z_3 = (sum(grades[2])/(len(grades[2])))
z_4 = (sum(grades[3])/(len(grades[3])))
z_5 = (sum(grades[4])/(len(grades[4])))
dict_stud.update({list_stud[0]: z_1})
dict_stud.update({list_stud[1]: z_2})
dict_stud.update({list_stud[2]: z_3})
dict_stud.update({list_stud[3]: z_4})
dict_stud.update({list_stud[4]: z_5})
print(dict_stud)

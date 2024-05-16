num = 11
str_ = ''

for i in range(1, 20):
    for j in range(1, 20):
        if num % (i+j) == 0 and i != j and i < j:
            str_ += str(i) + str(j)


print(str_)
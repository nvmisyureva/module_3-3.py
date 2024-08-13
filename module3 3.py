#Самостоятельная работа по уроку "Распаковка позиционных параметров".
#Задача "Распаковка"

def print_params(a=1,b = 'строка', c = True):
    print(a,b,c)

print_params()
print_params(b=25,c=[1,2,3])
print_params(b=25)
print_params(c=[1,2,3])

values_list = [22,'атом', False]
values_dict = {'a':232, 'b':49, 'c':[10,20,30,40,50]}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [5, 'urok']
print_params(*values_list_2,42)

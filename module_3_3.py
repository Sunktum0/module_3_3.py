def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

values_list = (134, 136.6, 'Кронштад')
values_dict = {'a' : 25, 'b' : False, 'c' : 'Москва'}
values_list_2 = ('Привет', 46)
print_params(8, 'Romled')
print_params( 1,True, False)
print_params(26)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)


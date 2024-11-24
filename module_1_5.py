immutable_var=1,'два',3.0,True
print(immutable_var)
print(f'Элементы класса {type(immutable_var)} неизменяемы')
mutable_list=[1,'два',3.0,True]
print(mutable_list)
mutable_list[1]=2
mutable_list.remove(3.0)
mutable_list.pop()
mutable_list.append('Modified')
print(mutable_list)

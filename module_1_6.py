my_dict={'Andrey':1996, 'Barbara':2003, 'Coco':1976, 'Dmitriy':2012}
print(my_dict)
print(my_dict['Barbara'])
print(my_dict.get('Vladimir','Такого имени в списке нет'))
my_dict.update({'Elena':1981, 'Tamara':1953})
print(my_dict.pop('Coco'))
print(my_dict)

my_set={2,1,8,3,4,5,2,3,7,'Int'}
print(my_set)
my_set.add(9)
my_set.add(6)
my_set.remove('Int')
print(my_set)
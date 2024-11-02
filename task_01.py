from models.linked_list import LinkedList

# функції в середині файла models/linked_list.py, тут використання
llist1 = LinkedList()

llist1.insert_at_beginning(17)
llist1.insert_at_end(5)
llist1.insert_at_end(6)
llist1.insert_at_end(9)
llist1.insert_at_end(1)
llist1.insert_at_end(10)
llist1.insert_at_end(15)
llist1.insert_at_end(16)
llist1.insert_at_end(18)

llist1.print_list()
print('-----------')

llist1.reverse_list() # функція для реверсування
llist1.print_list()
print('-----------')

b = llist1.sort() # функція для сортування (в середині використовує функцію що обʼєднює відсортовані списки)
b.print_list()

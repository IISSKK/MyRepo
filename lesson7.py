# read = open("test.txt", 'r', encoding= 'utf-8')
# result = read.read()
# print(result)
# read.close

# write_file = open('geeks.txt', 'w', encoding='utf-8')
# write_file.write('hello')
# write_file.close

# add = open('geeks.txt', 'a', encoding='utf-8')
# add.write('\nКак дела')
# add.close

# with open('geeks', 'r', encoding='utf-8') as with_read:
#     result = with_read.read()
#     print(result)


with open('geeks.pro.txt', 'w', encoding='utf-8') as me_myself:
    me = me_myself.write('Имя: Искендер\nФамилия: Исаков\nОпыт игры: 4 год\nНаправления: Python')
    print(me)


with open('exp.py', 'w', encoding='utf-8') as my_code:
    my = my_code.write("mine = input('Пиши свое имя: ')")
    my = my_code.write("\nprint(mine)")


with open('exp2.py', 'w', encoding='utf-8') as my_code2:
    my2 = my_code2.write('numbers = [1,2,3,4,5,6]\nfor num in numbers:\n    print(num*2)')

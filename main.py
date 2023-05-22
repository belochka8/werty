from random import shuffle
spisog_omg = ['соль',' перец', ' картошка']
triks = input('Введи ингридиенты (хорош - стоп):')

while triks != 'хорош':
    if triks in spisog_omg:
        print('Уже есть!!')

    else:
        spisog.omg.append(triks) 

    triks = input('Введи ингридиенты (хорош - стоп):')

spisok_blender = []
nums = int(input('Сколько месим ингредиентов:'))
for i in range(nums):
    shuffle(spisog_omg)
    spisok_blender.append(spisog_omg[0])
    spisok_omg.remove(spisok_omg[0])

print('Приготовь что-нибудь из:')
for i in range (nums):
    print(spisok_blender[i])


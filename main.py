
with open('recipes.txt') as file:
    cook_book  = {}
    for recipe in file:
        recipe_list = recipe.strip()
        quantity_of_ingredients = int(file.readline(2))
        volue_list = []
        for i in range(quantity_of_ingredients):
            a,b,c = file.readline().strip().split('|')
            volue_list.append({'ingredient_name': a, 'quantity': b, 'measure': c})
            cook_book [recipe_list] = volue_list
        file.readline()
print()

def get_shop_list_by_dishes(dishes, person_count):
    dict_1 = {}
    for dish in dishes:
        for key_and_val in cook_book.items():
            if key_and_val[0] == dish:
                for dict_ in key_and_val[1]:
                    the_native = list(dict_.items())
                    if the_native[0][1] not in dict_1:
                        dict_1[the_native[0][1]] = {the_native[2][0]: the_native[2][1],
                                                    the_native[1][0]: int(the_native[1][1] )* person_count}
                    else:
                        count = 0
                        for l in dict_1[the_native[0][1]].values():
                             count = l
                        dict_1[the_native[0][1]] = {the_native[2][0]: the_native[2][1],
                                                    the_native[1][0]: (count +(int(the_native[1][1]) * person_count))}
    print(dict_1)
get_shop_list_by_dishes(['Запеченный картофель', 'Фахитос'], 2)

files = ['1.txt', '2.txt', '3.txt']
files_list = []
for file in files:
    with open(file) as f:
        b = []
        for d in f:
            b.append(d.strip())
        files_list.append(b)
a = len(files_list[0])
b = len(files_list[1])
c = len(files_list[2])
a1 = "\n".join(files_list[0])
b1 = "\n".join(files_list[1])
c1 = "\n".join(files_list[2])

with open('finish_file.txt', 'a') as file4:
    count1 = 0
    count = 0
    while count1 < 3:
        if count == 0:
            if a < b and a < c:
                count = a
                count1 +=1
                file4.write(f"'1.txt'\n {a}\n {a1}\n")
            elif b < a and b < c:
                count = b
                file4.write(f"'2.txt'\n {b}\n {b1}\n")
                count1 += 1
            elif c > a and c > b:
                count = c
                file4.write(f"'3.txt'\n {c}\n {c1}\n")
                count1 += 1
        else:
            if (c > count and (c < a or c < b)) or (count1 >= 2 and (c > a and c > b)):
                file4.write(f"'3.txt'\n {c}\n {c1}\n")
                count1 += 1
                count = c
            elif (a > count and (a < c or a < b)) or (count1 >= 2 and (a > c and a > b)):
                file4.write(f"'1.txt'\n {a}\n {a1}\n")
                count1 += 1
                count = a
            elif (b > count and (b < a or b < c)) or (count1 >= 2 and (b > a and b > c)):
                file4.write(f"'2.txt'\n {b}\n {b1}\n")
                count1 += 1
                count = b













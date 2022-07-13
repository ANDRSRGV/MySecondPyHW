
with open('recipe.txt', 'r', encoding='utf-8') as data:
    cook_book = {}
    new_rec = True
    rec = []
    for line in data:
        if line == '\n':
            new_rec = True
            cook_book[rec_name] = rec
            rec = []
        else:
            if new_rec == True:
                rec_name = line.strip()
                cook_book.setdefault(rec_name)
                rec_ingr_count = data.readline()
                new_rec = False
            else:
                rec_list = []
                rec_list = line.split('|')
                rec_dict = {}
                rec_dict['ingredient_name'] = rec_list[0].strip()
                rec_dict['quantity'] = int(rec_list[1].strip())
                rec_dict['measure'] = rec_list[2].strip()
                rec.append(rec_dict)
    cook_book[rec_name] = rec
    print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    ing_dict = {}
    for rec in dishes:
        for ingr in cook_book[rec]:
            ing_dict.setdefault(ingr['ingredient_name'], {'measure':ingr['measure'],'quantity':0})
            ing_dict[ingr['ingredient_name']]['quantity'] += ingr['quantity'] * person_count

    print(ing_dict)



get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)






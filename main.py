def rec_split(rec:str):
    rec_list = rec.split('|')
    rec_dict = {}
    rec_dict['ingredient_name'] = rec_list[0].strip()
    rec_dict['quantity'] = rec_list[1].strip()
    rec_dict['measure'] = rec_list[2].strip()
    return(rec_dict)

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
                rec_dishes_count = data.readline()
                new_rec = False
            else:
                rec_list = []
                rec_list = line.split('|')
                rec_dict = {}
                rec_dict['ingredient_name'] = rec_list[0].strip()
                rec_dict['quantity'] = rec_list[1].strip()
                rec_dict['measure'] = rec_list[2].strip()
                rec.append(rec_split(line))
    cook_book[rec_name] = rec
    print(cook_book)


class Cook:
    cook_book = {}
    with open('recipes.txt', encoding='utf-8') as file:
        cook = ''
        for l in file:
            l = l.strip()
            if l.isdigit():
                continue
            elif l and '|' not in l:
                cook_book[l] = []
                cook = l
            elif l and '|' in l:
                name, q, msure = l.split(" | ")
                cook_book.get(cook).append(dict(ingredient_name=name, quantity=int(q), measure=msure))

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = Cook.cook_book
    dish = dict()
    for d in dishes:
        if d in cook_book:
            for x in cook_book[d]:
                if x['ingredient_name'] not in dish:
                    g = dict()
                    g['measure'] = x['measure']
                    g['quantity'] = x['quantity'] * person_count
                    dish[x['ingredient_name']] = g
                else:
                    dish[x['ingredient_name']]['quantity'] = dish[x['ingredient_name']]['quantity'] + x['quantity'] * person_count
    print(dish)

get_shop_list_by_dishes(['Фахитос', 'Омлет'], 12)
"""3. Реализовать структуру данных «Товары». Она должна представлять собой
 список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у
 пользователя.

Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]

Далее необходимо собрать аналитику о товарах. Реализовать словарь,
в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.

Пример:
{
“названия”: [“компьютер”, “принтер”, “сканер”],
“цены”: [20000, 6000, 2000],
“количества”: [5, 2, 7],
“ед”: [“шт.”]
}"""

prod = ['название', 'цена', 'количество', 'eд']
param = [(i, {k: input(f'{k}: ') for k in prod}) for i in range(1, 4)]

for i in param:
    print(i)

prod_dict = {}

for i, el in enumerate(list(param[0][1].keys())):
    prod_dict[el] = []

for i, el in enumerate(prod_dict):
    dict_list = []

    for j, el_prod in enumerate(param):
        key_val = el_prod[1].get(el)

        if key_val not in dict_list:
            dict_list.append(key_val)

    prod_dict[el] = dict_list

print(prod_dict)

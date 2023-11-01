# TODO Напишите функцию для поиска индекса товара


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

def is_item_in_list(items_list,find_item):
    for i in range(0,len(items_list)):
        if find_item == items_list[i]:
            return i





for find_item in ['банан', 'груша', 'персик']:

    index_item = is_item_in_list(items_list,find_item)  # TODO Вызовите функцию, что получить индекс товара

    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")

# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

def find_common_participants(first_group,second_group ,sep=','):
    first_group = first_group.split(sep)
    second_group = second_group .split(sep)

    setted_group_list = list(set(second_group) & set(first_group))
    common_list_of_participants = sorted(setted_group_list)

    return common_list_of_participants


print(find_common_participants(participants_first_group,participants_second_group,'|'))

# TODO Провеьте работу функции с разделителем отличным от запятой

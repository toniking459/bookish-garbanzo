list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
#sizeOfList = len(list_players)
#
#
# listTeamFirst = []
# listTeamSecond = []
#
#
# for i in range (- 1, sizeOfList -1):
#     if i%2 == 0:
#         listTeamFirst.append(list_players[i])
#     else:
#         listTeamSecond.append(list_players[i])
#
#
# print ("Первая команда: ", listTeamFirst,
#        "\n"
#        "Вторая команда: ", listTeamSecond)
#
#
listTeamFirst = list_players[      :(len(list_players))//2]
listTeamSecond = list_players[(len(list_players))//2:    ]
print(listTeamFirst)
print(listTeamSecond)


# TODO Разделите участников на две команды

users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']


dictUsers = \
    {
        "Общее количество": 0 ,
        "Уникальные посещения": 0
    }

sizeOfUsers = len(users)
amountOfUnique = len(set(users))

dictUsers["Общее количество"] = sizeOfUsers
dictUsers["Уникальные посещения"] = amountOfUnique


print(dictUsers)





# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений

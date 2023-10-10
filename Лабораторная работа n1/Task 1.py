numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
sumOfArray = 0
sizeOfArray = 0


for i in range(-1, len(numbers) - 1):
    if numbers[i] == None:
        wrongElement = i
        numbers[wrongElement] = 0
    sumOfArray += int(numbers[i])
    sizeOfArray += 1



averageValue = sumOfArray / sizeOfArray
numbers[wrongElement] = averageValue
#print ("Сумма всех элементов массива: ",sumOfArray)
#print ("Размер массива: ",sizeOfArray)
#print("Среднее арифметическое для массива numbers: ",averageValue)

# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)

# TODO Найдите количество книг, которое можно разместить на дискете
informationalSizeOfDisk = 1.44 * 1024 * 1024
amountOfPages = 100
amountOfLinesOnPage = 50
amountOfSymbOnTheLine = 25
sizeOfSymb = 4


sizeOfBook = amountOfLinesOnPage * amountOfPages * amountOfSymbOnTheLine * sizeOfSymb
amountOfBooksOnDisk = int(informationalSizeOfDisk // sizeOfBook)

print("Количество книг, помещающихся на дискету:", amountOfBooksOnDisk)

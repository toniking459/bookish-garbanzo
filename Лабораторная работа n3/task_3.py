# TODO  Напишите функцию count_letters
def count_letters(text):
    letters_dict = {}
    text = text.lower()
    for letter in text:
        if letter.isalpha():
            if letter not in letters_dict:
                letters_dict[letter]=1
            else:
                letters_dict[letter]+=1
    return letters_dict

# TODO Напишите функцию calculate_frequency
def calculate_frequency(letters_dict, text):
    letters_amount = 0
    for letter in text:
        if letter.isalpha():
            letters_amount+=1

    for key in letters_dict.keys():
        letters_dict[key]=round(letters_dict[key]/letters_amount,2)
    return letters_dict


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
main_dictionary = count_letters(main_str)
main_dictionary = calculate_frequency(main_dictionary,main_str)
for key in main_dictionary.keys():
    if str(main_dictionary[key]) == "0.0":
        main_dictionary[key] = "0.00"

    print(str(key) + ":", main_dictionary[key])
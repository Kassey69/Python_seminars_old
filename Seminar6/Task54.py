# 43 Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# входные и выходные данные хранятся в отдельных текстовых файлах
# aaaaddbbb  - 4a2d3b


with open('text1.txt', 'r') as data:
    text = data.read()


# text = 'ssssskkkkkfryyyyyttt'
def sets(text):
    lists = [text[i] for i in range(len(text))] # ['a', 'a', 'a', 'a', 'd', 'd', 'b', 'b', 'b']
    # print(lists)
    # r = (max(set(lists[x]), key = lambda x: lists.count(x)))
    # return r
    analize = ''
    counts = 1
    for i in range(len(lists)-1):
        if lists[i] == lists[i+1]:
            counts += 1
        else:
            analize += str(counts) +  lists[i]
            counts = 1 # обнуляем counts
       
    if counts > 1 or (lists[len(lists)-2] != lists[-1]):
        analize +=  str(counts) + lists[-1]
    return analize

def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha(): # Метод str.isalpha()проверяет, что строка состоит только из буквенных символов.
            number += txt[i]
        else:
            res += txt[i] * int(number) # сначала все aaaa потом aaaadddddd и так далее
            number = '' # чтоб не зависло все. очень много символов полетит
    return res

print(f'Сжатый модуль {sets(text)}')
print(f'Восстановлдение данных {decoding(sets(text))}')



with open('text2.txt', 'w') as data: # ну а тут открываем файл и принудительно записываем в него
    data.write(sets(text))



























# with open('42_RLE1_decoded.txt', 'r') as data:
#     my_text = data.read()

# my_text = 'ewfweefwfwefwe'
# def encode_rle(ss):
#     str_code = ''
#     prev_char = ''
#     count = 1
#     for char in ss:
#         if char != prev_char:
#             if prev_char:
#                 str_code += str(count) + prev_char
#             count = 1
#             prev_char = char
#         else:
#             count += 1
#     return str_code

            
# str_code = encode_rle(my_text)
# print(str_code)

# # with open('42_RLE2_encoded.txt', 'r') as data:
# #     my_text2 = data.read()

# my_text2 = '3232r2'

# def decoding_rle(ss:str):
#     count = ''
#     str_decode = ''
#     for char in ss:
#         if char.isdigit():
#             count += char 
#         else:
#             str_decode += char * int(count)
#             count = ''
#     return str_decode

# str_decode = decoding_rle(my_text2)
# print(str_decode)
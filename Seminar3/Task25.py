# # Константы
# colors = ('#fff', '#000', '#555')
# colors.append('uno')  # append  не поддерживает добавление
# print(colors)

# Словари
colors = {
    'bla-bla': 100,
    10.0: 'ключ'
} #  значение и ключ, ключ и значение через двоеточие
print(colors)
print(colors.get('bla-bla'))
# ссылка на ключи - https://pythonworld.ru/tipy-dannyx-v-python/slovari-dict-funkcii-i-metody-slovarej.html
colors = {
    'bla-bla': 100,
    10.0: 'ключ'}
def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
print(get_key(colors, 100))
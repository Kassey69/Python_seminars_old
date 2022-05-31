# Запись данных в файл Task24_file.txt

# with open('Task24_file.txt','w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')
colors = ['red', 'green', 'blue']
data = open('Task24_file.txt', 'w') #сдесь указываем режим, в котором будем работать
data.writelines(colors) # разделителей не будет
data.close()

path = 'Task24_file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()
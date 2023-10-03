''''
count_mas = int(input("Введите количество массивов: "))
mas_mas = []

for i in range(count_mas): #Заполнение массива массивами
    k = list(map(str, input().split()))
    mas_mas.append(k)

'''


def count_equals(mas_mas, count_mas):
    result_mas = []
    for i in range(count_mas-1):
        sim = i+1
        while(sim < count_mas):
            result = len(list(set(mas_mas[i]) & set(mas_mas[sim])))
            print("Общее количество элементов у " + str(i+1) + " и " + str(sim+1) + " строк: " + str(result))
            sim += 1
            result_mas.append(result)
    return result_mas
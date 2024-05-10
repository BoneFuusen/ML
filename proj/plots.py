import pickle

with open("graphs/list_of_generated_matrices", "rb") as file:
    graphs1 = pickle.load(file)
with open("graphs/list_of_largeGenerated_matrices", "rb") as file:
    graphs2 = pickle.load(file)

graphs = graphs1 + graphs2
graphs_nodes_count = []
for i in graphs:
    graphs_nodes_count.append(len(i))


with open("graphs/list_of_generatedGraphs_color_counts", "rb") as file:
    colours1 = pickle.load(file)
with open("graphs/list_of_largeGeneratedGraphs_color_counts", "rb") as file:
    colours2 = pickle.load(file)

primary_colours_count = colours1+colours2

with open("graphs/list_of_test_colours.rtf", "r") as file:
    test_colours_count1 = file.read().splitlines()
test_colours_count1 = [int(item) for item in test_colours_count1]
with open("graphs/list_of_test_colours_LARGE.rtf", "r") as file:
    test_colours_count2 = file.read().splitlines()
test_colours_count2 = [int(item) for item in test_colours_count2]

test_colours_count = test_colours_count2 + test_colours_count1


with open("graphs/list_of_generatedGraphs_time_requires", "rb") as file:
    times1 = pickle.load(file)
with open("graphs/list_of_largeGeneratedGraphs_time_requires", "rb") as file:
    times2 = pickle.load(file)

primary_times = times1 + times2

with open("graphs/list_of_test_times.rtf", "r") as file:
    test_times1 = file.read().splitlines()
test_times1 = [float(item) for item in test_times1]
with open("graphs/list_of_test_times_LARGE.rtf", "r") as file:
    test_times2 = file.read().splitlines()
test_times2 = [float(item) for item in test_times2]

test_times = test_times2 + test_times1

with open("list_of_prim_times.rtf", "w") as file:
    for i in primary_times:
        file.write(str(i) + "\n")
# import matplotlib.pyplot as plt
#
# # Сортировка данных по возрастанию количества нодов
# sorted_data = sorted(zip(graphs_nodes_count, primary_times, test_times))
# sorted_graphs_nodes_count, sorted_primary_times, sorted_test_times = zip(*sorted_data)
#
# # Вычисление отношения первоначальных цветов к тестовым в процентах
# ratios = [(primary / test * 100 if test != 0 else 0) for primary, test in zip(sorted_primary_times, sorted_test_times)]
#
# # Создание фигуры и осей
# fig, ax = plt.subplots()
#
# # Построение графика
# ax.plot(sorted_graphs_nodes_count, ratios)
#
# # Настройка осей и заголовка
# ax.set_xlabel('Количество нодов')
# ax.set_ylabel('Отношение первоначального времени к тестовому (в %)')
# ax.set_title('Отношение затраченного времени от кол-ва нодов')
#
# # Отображение графика
# plt.show()






import time


def greedy_graph_coloring(adj_matrix):
    start_time = time.time()  # Начальное время
    n = len(adj_matrix)
    colors = [0] * n  # Инициализируем список цветов нулями

    # Функция для проверки, был ли цвет присвоен соседям вершины
    def is_safe_color(node, color):
        for neighbor in range(n):
            if adj_matrix[node][neighbor] == 1 and color == colors[neighbor]:
                return False
        return True

    # Функция для присвоения цветов вершинам
    def color_graph():
        result = 0
        for node in range(n):
            # Назначаем первый доступный цвет для текущей вершины
            assigned = False
            color = 1
            while not assigned:
                if is_safe_color(node, color):
                    colors[node] = color
                    assigned = True
                else:
                    color += 1

            # Обновляем результат максимальным использованным цветом
            result = max(result, color)
        return result

    min_colors = color_graph()
    end_time = time.time()  # Конечное время
    execution_time = end_time - start_time

    return min_colors, execution_time


import pickle

from coloring import greedy_graph_coloring

with open("graphs/list_of_largeGenerated_matrices", "rb") as file:
    graphs = pickle.load(file)
with open("graphs/list_of_largeGeneratedGraphs_color_counts", "rb") as file2:
    color_counts = pickle.load(file2)
with open("graphs/list_of_largeGeneratedGraphs_time_requires", "rb") as file3:
    time_requires = pickle.load(file3)

with open("report_large.rtf", "w") as file:
    for i in range(0, len(graphs)):
        clrs, times = greedy_graph_coloring(graphs[i])

        file.write(f"Graph number {i+1} \n"
                   f"Graph nodes number: {len(graphs[i])} \n"
                   f"\n"
                   f"Primal colours number: {color_counts[i]} \n"
                   f"Primal time requirement: {time_requires[i]} \n"
                   f"\n"
                   f"Colours number: {clrs} \n"
                   f"Time requirement: {times} \n"
                   f"----------------------------------------------------------- \n")

with open("graphs/list_of_test_colours_LARGE.rtf", "w") as file:
    for i in range(0, len(graphs)):
        clrs, times = greedy_graph_coloring(graphs[i])

        file.write(str(clrs) + "\n")

with open("graphs/list_of_test_times_LARGE.rtf", "w") as file:
    for i in range(0, len(graphs)):
        clrs, times = greedy_graph_coloring(graphs[i])

        file.write(f"{times:.{16}f} \n")


# print(graphs[1])
# print(f"Primal colours number: {color_counts[1]}")
# print(f"Primal time requirement: {time_requires[1]} seconds")
# print("")

import numpy as np
import matplotlib.pyplot as plt

# Implementation of Segmented least squares using Matplotlib to display the results.

def segmented_least_squares(points, c):
    num_points = len(points)
    OPT = [[0, [], []] for _ in range(num_points)]

    for j in range(num_points):
        min = [float('inf'), []]
        for i in range(j):
            segment_points = points[i:j + 1]
            n = len(segment_points)

            sum_x = sum([segment_points[_][0] for _ in range(n)])
            sum_y = sum([segment_points[_][1] for _ in range(n)])
            sum_xy = sum([segment_points[_][0] * segment_points[_][1] for _ in range(n)])
            sum_x2 = sum([segment_points[_][0] ** 2 for _ in range(n)])

            a = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
            b = (sum_y - a * sum_x) / n

            e_ij = sum([(segment_points[_][1] - a * segment_points[_][0] - b) ** 2 for _ in range(n)])
            
            error = e_ij + c + OPT[i][0]

            if error < min[0]:
                min = [error, OPT[i][1] + [(i, j)], OPT[i][2] + [(e_ij, a, b)]]
                OPT[j] = min

    return OPT[num_points - 1]


def display_results(points, result, c):
    x = []
    y = []

    for i in range(len(result[1])):
        start = result[1][i][0]
        end = result[1][i][1]

        x.append(points[start][0])
        y.append(result[2][i][1] * points[start][0] + result[2][i][2])

        x.append(points[end][0])
        y.append(result[2][i][1] * points[end][0] + result[2][i][2])

    plt.scatter(*zip(*points), label='Points received')
    plt.plot(x, y, color='orange', label='Line minimizing the mean square error' )

    plt.xlabel('x', fontweight='bold', fontsize=12) 
    plt.ylabel('y', fontweight='bold', fontsize=12)
    plt.plot([],  label=f'Constant: {c}')
    plt.title('Segmented least squares', fontweight='bold', fontsize=16)

    plt.legend()
    plt.show()


# DATA 
points = [
    (1, 20.214),
    (2, 18.413),
    (3, 15.754),
    (4, 14.125),
    (5, 14.024),
    (6, 13.226),
    (7, 15.458),
    (8, 14.547),
    (9, 14.754),
    (10, 13.536),
    (11, 12.425),
    (12, 10.543),
    (13, 10.058),
    (14, 9.135),
    (15, 7.698),
    (16, 5.564),
    (17, 4.213),
    (18, 3.896),
    (19, 6.012),
    (20, 7.894),
    (21, 10.214),
    (22, 12.266),
    (23, 15.124),
    (25, 16.989),
    (26, 19.014),
    (27, 21.254),
    (28, 22.887),
    (29, 24.364),
    (30, 25.898)
]

c = 0
display_results(points, segmented_least_squares(points, c), c)





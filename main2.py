import matplotlib.pyplot as plt
import matplotlib.pyplot as pyplotlt
import numpy as np


A = np.array([[-10.3, 10.2],
              [4.7, 12.3],
              [13.2, 8.8]])

B = np.array([70, 173, 282])

# Отримання значень x1 та x2
x1_values = np.linspace(-15, 20, 100)
x2_values_eq1 = (70 - (-10.3) * x1_values) / 10.2
x2_values_eq2 = (173 - 4.7 * x1_values) / 12.3
x2_values_eq3 = (282 - 13.2 * x1_values) / 8.8



intersection_points = []
for i in range(len(A)-1):
    for j in range(i+1, len(A)):
        X = np.linalg.solve(np.vstack([A[i], A[j]]), np.array([B[i], B[j]]))
        intersection_points.append(X)


x1_intersect = [point[0] for point in intersection_points]
x2_intersect = [point[1] for point in intersection_points]




plt.figure(figsize=(8, 16))

plt.plot(x1_values, x2_values_eq1,'r:', label='f[0]')
plt.plot(x1_values, x2_values_eq2, '--c', label='f[1]')
plt.plot(x1_values, x2_values_eq3, '-.k', label='f[2]')


# plt.fill_between(x1_values, x2_values_eq1, color='blue', alpha=0.2)
# plt.fill_between(x1_values, x2_values_eq2, color='green', alpha=0.2)
# plt.fill_between(x1_values, x2_values_eq3, color='yellow', alpha=0.2)

plt.annotate('-10.3*x1 + 10.2*x2 = 70', xy=(10, 19), rotation=27, fontsize=8, color='black')
plt.annotate('4.7*x1 + 12.3*x2 = 173', xy=(6, 9.5), rotation=-13, fontsize=8, color='black')
plt.annotate('13.2*x1 + 8.8*x2 = 282', xy=(-4, 30), rotation=-40, fontsize=8, color='black')



plt.fill(x1_intersect, x2_intersect, color='orange', alpha=0.3)


# for point in intersection_points:
#     plt.plot(point[0], point[1], 'ro')
#     plt.annotate("The intersection point of f[] and f[]", xy=(point[0], point[1]), xytext=(-20, 20),
#                  textcoords='offset points', color='black', fontsize=8,
#                  arrowprops=dict(arrowstyle="->", color='black',))


intersection_points = np.array(intersection_points)

plt.plot(intersection_points[:, 0], intersection_points[:, 1], 'ro')
plt.annotate("The intersection point of f[0] and f[1]", xy=(intersection_points[0, 0], intersection_points[0, 1]), xytext=(-200, 100),
             textcoords = 'offset points', color = 'black', fontsize = 8,
             arrowprops = dict(arrowstyle = "->", color = 'black'))

plt.annotate("The intersection point of f[0] and f[2]", xy=(intersection_points[1, 0], intersection_points[1, 1]), xytext=(-150, 200),
             textcoords = 'offset points', color = 'black', fontsize = 8,
             arrowprops = dict(arrowstyle = "->", color = 'black'))

plt.annotate("The intersection point of f[1] and f[2]", xy=(intersection_points[2, 0], intersection_points[2, 1]), xytext=(-150, 300),
             textcoords = 'offset points', color = 'black', fontsize = 8,
             arrowprops = dict(arrowstyle = "->", color = 'black',))




plt.xlabel('x1')
plt.ylabel('x2')



plt.legend()
plt.grid(True)
plt.grid(color='lime', alpha=0.4, linestyle='dashed')
#plt.savefig('plot.svg', dpi=100)
plt.show()
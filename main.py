import matplotlib.pyplot as plt
import matplotlib.pyplot as pyplotlt
import numpy as np

N = ord('A') % 10 + 1
print(N)

# – 10.3 x1 + 10.2 x2 = 70
# 4.7 x1 + 12.3 x2 = 173
# 13.2 x1 + 8.8 x2 = 282




A = np.array([[-10.3, 10.2],
              [4.7, 12.3],
              [13.2, 8.8]])

# Создаем вектор правой части
B = np.array([70, 173, 282])




# Отримання значень x1 та x2
x1_values = np.linspace(0, 20, 100)
x2_values_eq1 = (70 - (-10.3) * x1_values) / 10.2
x2_values_eq2 = (173 - 4.7 * x1_values) / 12.3
x2_values_eq3 = (282 - 13.2 * x1_values) / 8.8


plt.figure(figsize=(10, 6))

plt.subplot(2,3,1)
plt.plot(x1_values, x2_values_eq1,'r:')
plt.title('-10.3x1 + 10.2x2 = 70')
plt.grid(True)
plt.ylim(-40, 80)


plt.subplot(2,3,2)
plt.plot(x1_values,x2_values_eq2,'--c' )
plt.title('4.7x1 + 12.3x2 = 173')
plt.grid(True)
plt.ylim(-40, 80)


plt.subplot(2,3,3)
plt.plot(x1_values, x2_values_eq3,'-.k')
plt.title('13.2x1 + 8.8x2 = 282')
plt.ylim(-40, 80)
plt.grid(True)

plt.tight_layout()
plt.show()
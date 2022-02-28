#погружение в python
#неделя 1 задание 3
#корни квадратного уравнения

import sys
import math

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

d = b * b - 4 * a * c

x_1 = (-b + math.sqrt(d)) / (2 * a)
x_2 = (-b - math.sqrt(d)) / (2 * a)

print(int(x_1))
print(int(x_2))
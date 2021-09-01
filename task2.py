#погружение в python
#неделя 1 задание 2
#рисуем лестницу

import sys

numb = sys.argv[1]

for i in range(1, int(numb)+1):
    #i = int(i)
    print('{}{}'.format(' '*(int(numb)-i), '#'*i))
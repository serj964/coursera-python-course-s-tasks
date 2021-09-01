#погружение в python
#неделя 1 задание 1
#сумма цифр в строке

import sys

digit_string = sys.argv[1]

ans = 0
for i in range(len(digit_string)):
    ans += int(digit_string[i])
    
print(ans)
    
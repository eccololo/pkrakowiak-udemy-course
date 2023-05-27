"""
Napisz program, który wydrukuje do konsoli 10
pierwszych liczb pierwszych rozdzielonych przecinkiem.
W rozwiązaniu użyj pętli while oraz instrukcji break.
"""
number = 0
counter = 1
output_list = []
while True:
    flag = True
    if number == 0 or number == 1:
        number += 1
        continue

    for i in range(2, number):
        if number % i == 0:
            flag = False
            break
    if flag:
        output_list.append(str(number))
    number += 1
    counter += 1
    if len(output_list) == 10:
        break

print(",".join(output_list))
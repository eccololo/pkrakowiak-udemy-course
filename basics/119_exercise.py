# Chcesz utworzyć program wyświetlający listę wszystkich plików z rozszerzeniem .py w bieżącym katalogu - oznaczenie bieżącego katalogu to '.'. Wykorzystaj w tym celu moduł wbudowany os. Każdą nazwę pliku wydrukuj w nowej linii tak jak pokazano poniżej.
#
#
#
# Oczekiwany wynik:
#
#
#
# exercise.py
# evaluate.py
# result.py
# run_unittest.py

import os

dir_list = os.listdir(".")
for item in dir_list:
    if item.endswith(".py"):
        print(item)
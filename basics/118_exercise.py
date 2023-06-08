# Chcesz utworzyć program wyświetlający listę wszystkich plików i folderów w bieżącym katalogu - oznaczenie bieżącego katalogu to '.'. Wykorzystaj w tym celu moduł wbudowany os. Każdą nazwę pliku lub folderu wydrukuj w nowej linii tak jak pokazano poniżej.
#
#
#
# Oczekiwany wynik:
#
#
#
# exercise.py
# evaluate.py
# __pycache__
# result.py
# run_unittest.py

import os

dir_list = os.listdir(os.getcwd())
for item in dir_list:
    print(item)
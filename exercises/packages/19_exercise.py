# Wykorzystując moduł wbudowany os w katalogu roboczym utwórz
# katalog o nazwie documents. Następnie w katalogu documents
# utwórz 12 katalogów dla każdego miesiąca o nazwach odpowiednio
# 01_sales, ..., 12_sales. W odpowiedzi wydrukuj posortowane
# nazwy katalogów w katalogu documents.

# import os
# months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
#
# # print(os.mkdir("documents"))
# # os.chdir("documents")
#
# # for month in months:
#     # os.mkdir(month + "_sales")
#
# all_path = os.path.join(os.getcwd(), "documents")
# print(os.listdir(all_path))


dirnames = [f'{str(i).zfill(2)}_sales' for i in range(1, 13)]

print(dirnames)

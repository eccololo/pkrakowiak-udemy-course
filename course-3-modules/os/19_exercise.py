import os

documents_path = os.path.join(os.getcwd(), 'documents')
if not os.path.exists(documents_path):
    os.mkdir(documents_path)

for i in range(1, 13):
    if i < 10:
        sales_dir = "0" + str(i) + "_sales"
    else:
        sales_dir = str(i) + "_sales"
    sales_dir_path = os.path.join(documents_path, sales_dir)
    if not os.path.exists(sales_dir_path):
        os.mkdir(sales_dir_path)

os.chdir(documents_path)
print(sorted(os.listdir(os.getcwd())))
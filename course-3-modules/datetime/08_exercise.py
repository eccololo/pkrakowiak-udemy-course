from datetime import datetime

date_str_1 = '3 March 1995'
date_str_2 = '3/9/1995'
date_str_3 = '21-07-2021'

datetime_obj_1 = datetime.strptime(date_str_1, "%d %B %Y")
datetime_obj_2 = datetime.strptime(date_str_2, "%d/%m/%Y")
datetime_obj_3 = datetime.strptime(date_str_3, "%d-%m-%Y")


print(datetime_obj_1)
print(datetime_obj_2)
print(datetime_obj_3)
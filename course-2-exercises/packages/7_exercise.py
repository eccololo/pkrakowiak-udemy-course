# 2021-04-20 11:30:00
#
#
# Na następujące formaty:
#
# 2021-04-20
# 20-04-2021
# 04-2021
# April-2021
# 20 April, 2021
# 2021-04-20 11:30:00
# 04/20/21 11:30:00
# 20(Tue) April 2021

import datetime

# print(help(datetime.datetime.strftime))

dt1 = datetime.datetime(2021, 4, 20, 11, 30, 0)

str1 = dt1.strftime("%Y-%m-%d")
str2 = dt1.strftime("%d-%m-%Y")
str3 = dt1.strftime("%m-%Y")
str4 = dt1.strftime("%B-%Y")
str5 = dt1.strftime("%d %B, %Y")
str6 = dt1.strftime("%Y-%m-%d %H:%M:%S")
str7 = dt1.strftime("%m/%d/%y %H:%M:%S")
str8 = dt1.strftime("%d(%a) %B %Y")

print(str1)
print(str2)
print(str3)
print(str4)
print(str5)
print(str6)
print(str7)
print(str8)

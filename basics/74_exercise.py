# Utwórz listę z podanych nazw technologii:
#
# 'python'
#
# 'java'
#
# 'sql'
#
# 'sas'
#
#
#
# Następnie zapisz każdy element listy w nowej linii pliku techs.txt. Oczekiwana zawartość pliku techs.txt:
#
#
#
# python
# java
# sql
# sas

techs = ['python', 'java', 'sql', 'sas']
with open("74_techs.txt", "w") as f:
    for tech in techs:
        f.write(tech + "\n")


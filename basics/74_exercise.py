# [IN]: ['python', 'java', 'sql', 'sas']
# [OUT]:  74_techs.txt file:
# python
# java
# sql
# sas


techs = ['python', 'java', 'sql', 'sas']
with open("74_techs.txt", "w") as f:
    for tech in techs:
        f.write(tech + "\n")


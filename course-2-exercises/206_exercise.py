techs = ['python', 'java', 'sql', 'sas']
with open("206_techs.txt", "w") as f:
    for item in techs:
        f.writelines(f"{item}\n")
hashtags = '#weekend#good#time#'
# Enter your solution here
splitted = hashtags.split("#")
for item in splitted:
    if item == "":
        continue
    print(item)
import re


html = """<!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">

  <title>The HTML5 Title</title>
  <meta name="description">

  <link rel="stylesheet" href="css/styles.css?v=1.0">

</head>

<body>
  <script src="js/scripts.js"></script>
</body>
</html>"""

match_list = re.findall(pattern="<\/*[a-zA-Z =\"-?]+", string=html)

for item in match_list:
    print(item)
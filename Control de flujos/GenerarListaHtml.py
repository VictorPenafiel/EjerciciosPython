import sys
# inicio del html
html = "<ul>\n"
items = int(sys.argv[1])
i = 1 # valor inicial
while i <= items:
    html += f"\t<li> {i} </li>\n"
    i += 1
# final del html
html += "</ul>"
print(html)

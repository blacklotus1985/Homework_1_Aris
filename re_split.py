# reject pattern to split for dot or for comma
regex_pattern = r'\.|,'


import re
print("\n".join(re.split(regex_pattern, input())))



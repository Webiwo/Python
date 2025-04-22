import re

# password
# check at https://regex101.com/
pattern = re.compile(r"[A-Za-z0-9@#$]{8,}\d")
password = "asFG45#n$KAw6"

check = pattern.fullmatch(password)
print(check)

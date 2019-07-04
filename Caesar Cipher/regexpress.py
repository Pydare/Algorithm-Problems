import re

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters  (Need to be escaped):
.[{()\^$|?*+


coreyms.com

321--555-4321
123.555.1234
123*555*1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs Joyce
Mr T
'''

url = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''
pattern = re.compile(r'https?://(www\.)?[a-zA-Z]+\.(com|gov)')
matches = pattern.finditer(url)

for match in matches:
    print(match.group(1))

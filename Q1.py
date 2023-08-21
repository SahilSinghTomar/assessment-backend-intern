import re

contact_no = '''
2124567890
212-456-7890
(212)456-7890
(212)-456-7890
212.456.7890
212 456 7890
+12124567890
+12124567890
+1 212.456.7890
+212-456-7890
1-212-456-7890
'''

pattern = re.compile(r'(\+1|1|\(|\+)?[ -]?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}')

matches = pattern.finditer(contact_no)

ct = 0

for match in matches:
    ct += 1
    print(match)

print(f'No of matches: {ct}')

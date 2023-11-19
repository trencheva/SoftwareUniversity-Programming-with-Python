import re

single_string = input()
pattern = r'\s([a-z0-9][a-z0-9\.\-\_]+@[a-z][a-z\-\.]+\.[a-z]+\b)'
extracted_emails = re.findall(pattern, single_string)
if extracted_emails:
    for extracted_email in extracted_emails:
        print(extracted_email)

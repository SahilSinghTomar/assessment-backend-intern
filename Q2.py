import re
from bs4 import BeautifulSoup
import requests


def match_all(text):
    emails = []
    socials = []
    contacts = []

    email_pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
    contact_pattern = re.compile(r'(\+1|1|\(|\+)?[ -]?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}')
    socials_pattern = re.compile(r'https://www\.(facebook|linkedin|instagram|twitter)\.com/[^"\'>]+')

    email_matches = email_pattern.finditer(text)
    contact_matches = contact_pattern.finditer(text)
    socials_matches = socials_pattern.finditer(text)

    for match in email_matches:
        emails.append(match.group())

    for match in contact_matches:
        contacts.append(match.group())

    for match in socials_matches:
        socials.append(match.group())

    return [emails, socials, contacts]


url = input("Enter correct url of website: ")

try:
    html_code = requests.get(url).text
    soup = BeautifulSoup(html_code, 'lxml')

    output = match_all(str(soup))

    print("Social Links -")
    for i in output[1]:
        print(i)

    print()

    print("Emails -")
    for i in output[0]:
        print(i)

    print()

    print("Contact: ")
    for i in output[2]:
        print(i)

    print()


except requests.exceptions.RequestException as e:
    print("Error:", e)

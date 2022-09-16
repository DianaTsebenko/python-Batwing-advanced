import re

#  Task 1
print("------------------Task 1------------------")


def search_phone(text):
    """
    1. Write a Python program which search a phone numbers.
    Valid example: Hello, my phone number is 251-65-23.
    Invalid example: Henry Ford was born July 30, 1863, on a farm in Springwells Township, Michigan.
    """
    text = str(text)

    pattern = r'(\d{3}[-\.\s]??\d{2}[-\.\s]??\d{2})'
    res = re.findall(pattern, text)

    if res:
        print(res)
    else:
        print("Nothing")


arr = ["Hello, my phone number is 251-65-23.", "Hello, my phone number is 251 65 23.",
       "Henry Ford was born July 30, 1863, on a farm in Springwells " \
       "Township, Michigan."]

for i in arr:
    search_phone(i)

#  Task 2
print("------------------Task 2------------------")


def check_email(email):
    pattern = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    res = re.findall(pattern, email.lower())
    if res:
        print(res)
    else:
        print("Nothing")


arr2 = ["test@gmail.com", "diana1234@gmail.com", ".diana@gmail.com"]

for i in arr2:
    check_email(i)

#  Task 3
print("------------------Task 3------------------")

ip_1 = "216.008.094.190"
res = re.sub('(^|\.)0+(?=[^.])', r'\1', string=ip_1)
print(res)

#  Task 4
print("------------------Task 4------------------")


def check_ip_address(ip):
    pattern = r"^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[" \
              r"0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    if re.search(pattern, ip):
        print(f'{ip} - Valid IP')
    else:
        print(f'{ip} - Invalid IP')


arr_ip = ['128.120.94.112', '0.1.2.0', '0.0.0']

for i in arr_ip:
    check_ip_address(i)

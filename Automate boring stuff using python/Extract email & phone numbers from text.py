# program to find all the phone numbers/emails from the data copied on clipboard

# steps
# 1.1. regex for US phone number (type: xxx-xxx-xxxx)
# 1.2. regex for Indian phone number (type: XXXXXXXXXX, 0 XXXXXXXXXX, 0-XXXXXXXXXX, +91 XXXXXXXXXX, 91 XXXXXXXXXX, 91XXXXXXXXXX)
# 2. regex for email (type: som!_.1ething@some!_1thing.edu)
# 3. get the text off the clipboard
# 4. extract the email & phone from the text.
# 5. copy the text back to the clipboard.


import re

# US mobile number
# phone_regex = re.compile(r'''
# \d{3}-\d{3}-\d{4}
#    ''', re.VERBOSE)

# indian mobile number
phone_regex = re.compile('''
( 
 (0|0-|91|[+]91|[+]91\s)?        # country_code(optional)
 \d{10}         # mobile_number
)
    ''', re.VERBOSE)



email_regex = re.compile(r'''
[a-zA-Z0-9_.]+      # name part
@                   # @ symbol
[a-zA-Z0-9_.]+      # remaining part
''',re.VERBOSE)

text_india = '''
Capt. Bhanu Johri HOD (Operation) T: 01234567890
E: bhanu.johri@pawanhans.co.in
Capt. Bhanu Johri HOD (Operation) T: 911234567890
E: bhanu.johri@pawanhans.edu
Capt. Bhanu Johri HOD (Operation) T: +911234567890
E: bhanu.johri@pawanhans.co.in
Capt. Bhanu Johri HOD (Operation) T: +91 1234567890
E: bhanu.johri@pawanhans.com
Ajay Pahuja Manager (Operation) T: 0-1234567890
E: ajaypahuja1968@gmail.com
Capt. Rajeev Sharma Dy. Chief (Safety) T: 1234567890
E: rajeev.sharma@pawanhans.co.in
'''

extracted_phone = phone_regex.findall(text_india)
extracted_email = email_regex.findall(text_india)
phone_numbers = []
for phone_number in extracted_phone:
    phone_numbers.append(phone_number[0])
phone_numbers = '\n'.join(phone_numbers)
extracted_email = '\n'.join(extracted_email)

print(phone_numbers)
print(extracted_email)

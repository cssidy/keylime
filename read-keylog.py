import re

with open("keylog.txt", "r") as keylog:
    data = keylog.read()

    # use regex to separate out emails, passwords, and other vital information
    phoneRegex = re.compile('''(
        (\d{3}|\(\d{3}\))?              # area code
        (\s|-|\.)?                      # separator
        (\d{3})                         # first 3 digits
        (\s|-|\.)                       # separator
        (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
    )''', re.VERBOSE)

    emailRegex = re.compile('''(
        [a-zA-Z0-9._%+-]+               # username
        @                               # @ symbol
        [a-zA-Z0-9.-]+                  # domain name
        (\.[a-zA-Z]{2,4})               # dot-something
    )''', re.VERBOSE)


#    passwordRegex = re.compile('''(
#        ^(?=.*?\d)                      # at least one digit
#        (?=.*?[A-Z])                    # at lease one uppercase
#        (?=.*?[a-z])                    # at least one lowercase
#        [A-Za-z\d]{10,}$                # at least 10 characters
#    )''', re.VERBOSE)

    matches = []
    for groups in phoneRegex.findall(data):
        phoneNum = '-'.join([groups[1], groups[3], groups[5]])
        if groups[8] != '':
            phoneNum += ' x' + groups[8]
            matches.append(phoneNum)
    for groups in emailRegex.findall(data):
        matches.append(groups[0])

    if len(matches) > 0:
        print('\n'.join(matches))
    else:
        print('No phone numbers, email address or passwords found.')







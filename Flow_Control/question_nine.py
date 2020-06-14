"""
Prints 'Hello' if 1 is stored in the variable spam.
Prints 'Howdy' if 2 is stores in spam.
Prints 'Greetings!' id anything else is stored in spam.
"""

spam = input('Enter value for spam: ')

if int(spam) == 1:
    print('Hello')
elif int(spam) == 2:
    print('Howdy')
else:
    print('Greetings!')

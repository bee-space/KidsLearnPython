#!/usr/bin/python3

def check_user_mail(email):
    result = ''
    if(email == 'sychov.s@gmail.com'):
        result = 'Serhii Sychov'
    if(email == 'misha.tovstenko@gmail.com'):
        result = 'Misha Tovstenko'
    else:
        result = 'not found'
    return result

def check_user_name(name):
    if(name == 'Serhii Sychov'):
        return 'sychov.s@gmail.com'
    if(name == 'Misha Tovstenko'):
        return 'misha.tovstenko@gmail.com'
    else:
        return 'not found'


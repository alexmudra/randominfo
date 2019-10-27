from __future__ import unicode_literals
import sys, os
sys.path.append("/randominfo/")
from .Date_Time import Date_Time
from .Person import Person
from random import randint, choice, sample
from datetime import datetime


__title__ = 'randominfo'
__version__ = '0.1'
__author__ = 'Bhuvan Gandhi'
__license__ = 'MIT'

try:
    pass
except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fileName = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    if exc_type == TypeError:
        print(fileName + ": " + "Invalid argument list. - line-" + str(exc_tb.tb_lineno))
    else:
        print(e)

def get_digit_otp(len):
    otp = ""
    for _ in range(len):
        otp += str(randint(1,9))
    return otp

def get_chars_otp(len, lowerCase = True, upperCase = True):
    otp = ""
    chars = ""
    if lowerCase == True:
        if upperCase == True:
            chars = "QWERTYUIOPLKJHGFDSAZXCVBNMqwertyuioplkjhgfdsazxcvbnm"
        else:
            chars = "qwertyuioplkjhgfdsazxcvbnm"
    else:
        if upperCase == True:
            chars = "QWERTYUIOPLKJHGFDSAZXCVBNM"
        else:
            return "Invalid combination."
    for _ in range(len):
        otp += str(chars[randint(0, len(chars) - 1)])
    return otp

def get_otp(len):
    otp = ""
    chars = "QWERTYUIOPLKJHGFDSAZXCVBNMqwertyuioplkjhgfdsazxcvbnm0123456789"
    for _ in range(len):
        otp += str(chars[randint(0, len(chars) - 1)])
    return otp

def get_formatted_datetime(strDate, _format = "%d-%m-%Y %H:%M:%S"):
    return datetime.strptime(strDate, _format)

def get_email():
    domains = ["gmail", "yahoo", "hotmail", "express", "yandex", "nexus", "online", "omega", "institute", "finance", "company", "corporation", "community"]
    extentions = ['com', 'in', 'jp', 'us', 'uk', 'org', 'edu', 'au', 'de', 'co', 'me', 'biz', 'dev', 'ngo', 'site', 'xyz', 'zero', 'tech']
    if Person == None:
        prsn = Person()
    else:
        prsn = Person

    c = randint(0,2)
    dmn = choice(domains)
    ext = choice(extentions)

    if c == 0:
        email = prsn.first_name + get_formatted_datetime(prsn.birthdate(), "%Y") + dmn + "." + ext
    elif c == 1:
        email = prsn.last_name + get_formatted_datetime(prsn.birthdate(), "%d") + dmn + "." + ext
    else:
        email = prsn.first_name + get_formatted_datetime(prsn.birthdate(), "%y") + dmn + "." + ext
    return email

def random_password(length = 8, special_chars = True, digits = True):
    spec_chars = ['!', '@', '#', '$', '%', '^', '&', '*']
    alpha = "QWERTYUIOPLKJHGFDSAZXCVBNMmnbvcxzasdfghjklpoiuytrewq"
    spec_char_len = 0
    chars = ""
    if special_chars == True:
        spec_char_len = randint(1,3)
        for _ in range(spec_char_len):
            chars += choice(spec_chars)

    if digits == True:
        spec_char_len = randint(0,9)
        for _ in range(spec_char_len):
            chars += str(randint(0,9))

    for _ in range(length - spec_char_len):
        chars += choice(alpha[randint(0, len(alpha) - 1)])

    paswd = ''.join(sample(chars, len(chars)))
    return paswd

def get_phone_number(country_code = True):
    phone = ""
    if country_code == True:
        cCodes = [91, 144, 141, 1, 44, 86, 52, 61, 32, 20, 33, 62, 81, 31, 7]
        phone = "+"
        phone += str(choice(cCodes))
        phone += " "
    for i in range(0,10):
        if i == 0:
            phone += str(randint(8,9))
        else:
            phone += str(randint(0,9))
    return phone

'''
REFERENCE:
http://www.first-names-meanings.com/country-indian-names.html
https://www.familyeducation.com/baby-names/browse-origin/surname/indian
'''
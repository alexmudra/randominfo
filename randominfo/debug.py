import csv
import sys
from os.path import abspath, join, dirname
from random import randint

sys.path.append("/randominfo/")

from randominfo import get_first_name, get_last_name, get_full_name, get_gender, get_country, choice
# from random import randint, choice, sample, randrange
from _csv import Error, __version__, writer, reader, register_dialect, \
                 unregister_dialect, get_dialect, list_dialects, \
                 field_size_limit, \
                 QUOTE_MINIMAL, QUOTE_ALL, QUOTE_NONNUMERIC, QUOTE_NONE, \
                 __doc__
from _csv import Dialect as _Dialect

first_name = get_first_name(gender = None)
# last_name = get_last_name()
# full_name = get_full_name(gender = None)
# gender = get_gender(first_name)
# country = get_country(first_name = None)



full_path = lambda filename: abspath(join(dirname(__file__), filename))


# def get_country(first_name=None):
#     countryFile = csv.reader(open(full_path('data.csv'), 'r'))
#     country = ""
#     if first_name is not None:
#         for data in countryFile:
#             if data[0] != '' and data[0] == first_name:
#                 country = data[6]
#                 break
#         if country == "":
#             print("Specified user data is not available. Tip: Generate random country.")
#     else:
#         filteredData = []
#         for data in countryFile:
#             if data[0] != '':
#                 filteredData.append(data[6])
#             if filteredData == '':
#                 raise ValueError(f"Empty country data in {countryFile} row. Try again")
#         country = choice(filteredData)
#     return country


# def get_address():
#     full_addr = []
#     addrParam = ['street', 'landmark', 'area', 'city', 'state', 'country', 'pincode']
#
#     for i in range(4, 9):
#         addrFile = csv.reader(open(full_path('data.csv'), 'r'))
#         allAddrs = []
#
#         for addr in addrFile:
#             try:
#                 if addr[i] != '':
#                     allAddrs.append(addr[i])
#             except IndexError:
#                 print(f"Index error occurred for index {i}")
#
#         if len(allAddrs) == 0:
#             print(f"No data available for index {i}")
#         else:
#             full_addr.append(choice(allAddrs))
#
#     full_addr = dict(zip(addrParam, full_addr))
#     return full_addr


# def get_address():
#     full_addr = []
#     addrParam = ['street', 'landmark', 'area', 'city', 'state', 'country', 'pincode']
#     for i in range(5,12):
#         addrFile = csv.reader(open(full_path('data.csv'), 'r'))
#         allAddrs = []
# 	    for addr in addrFile:
# 			try:
# 				if addr[i] != '':
# 					allAddrs.append(addr[i])
# 			except:
# 				pass
# 		full_addr.append(choice(allAddrs))
# 	full_addr = dict(zip(addrParam, full_addr))
# 	return full_addr


def get_hobbies():
	hobbiesFile = csv.reader(open(full_path('data.csv'), 'r'))
	allHobbies = []
	for data in hobbiesFile:
		if data[3] != '':
			allHobbies.append(data[3])
	hobbies = []
	for _ in range (1, randint(2,6)):
		hobbies.append(choice(allHobbies))
	return hobbies

g = get_hobbies()


if __name__ == "__main__":

    print(f"first_name -> {first_name}")
    print(f"hobbies -> {g}")
    # print(f"Random address -> {get_address()}")
    # print(f"last_name -> {last_name}")
    # print(f"full_name -> {full_name}")
    # print(f"get_gender -> {gender}")
    # print(f"get_country -> {country}")
    # print(f"get contry for {first_name} -> {get_country(first_name)}")


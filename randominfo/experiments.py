from randominfo import get_first_name, get_last_name, get_full_name, get_gender, get_country, get_birthdate, get_otp, \
get_today, get_address, get_hobbies

first_name = get_first_name(gender = None)
last_name = get_last_name()
full_name = get_full_name(gender = None)
gender = get_gender(first_name)
country = get_country(first_name = None)
birth_date = get_birthdate(startAge = None, endAge = None, _format = '%d %b, %Y')
random_temp_pass = get_otp(length = 6, digit = True, alpha = True, lowercase = True, uppercase = True)
today_date_time = get_today(_format ="%d-%m-%Y %H:%M:%S")
random_address = get_address()
generate_hobbies = get_hobbies()

if __name__ == "__main__":

    print(f"first_name -> {first_name}")
    print(f"last_name -> {last_name}")
    print(f"full_name -> {full_name}")
    print(f"get_gender -> {gender}")
    print(f"get_country -> {country}")
    print(f"get contry for {first_name} -> {get_country(first_name)}")
    print(f"get birth date for {first_name} -> {birth_date}")
    print(f"generate random_temp_pass for {first_name} -> {random_temp_pass}")
    print(f"Today date-time -> {today_date_time}")
    print(f"Random address -> {random_address}")
    print(f"Generate list of hobbies for {first_name} -> {generate_hobbies}")



 # phone number details project

import phonenumbers
from phonenumbers import carrier , geocoder , timezone

mobile_no = input('Enter your number with country code: ')
mobile_no = phonenumbers.parse(mobile_no)

# get timezone from phone number
print(timezone.time_zones_for_number(mobile_no))

# get carrier number from phone number
print(carrier.name_for_number(mobile_no, 'en'))

# get region information from phone number
print(geocoder.description_for_number(mobile_no, 'en'))

# validate phone number
print('valid mobile number: ' , phonenumbers.is_valid_number(mobile_no))

# checking possibilities of a number
print('checking possibilities of a number: ' , phonenumbers.is_possible_number(mobile_no))


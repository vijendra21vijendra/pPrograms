from phonenumbers import carrier
import phonenumbers
from phonenumbers import geocoder
# x = phonenumbers.parse("+919079999751", None)
# # x = phonenumbers.parse("+442083661177", None)
# print(x)

# from testnum import numbers
numbers = "+919079999751"
numbers = "+919982827357"

ch_number = phonenumbers.parse(numbers, 'CH')
print(numbers)
print(ch_number)
print(geocoder.description_for_number(ch_number, "en"))


service_nmbr = phonenumbers.parse(numbers, "RO")
print(carrier.name_for_number(service_nmbr, "en"))

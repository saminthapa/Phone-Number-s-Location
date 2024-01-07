import phonenumbers
from phonenumbers import timezone,carrier
number=input("number-")
phone=phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone,"en")
print(number)
print(phone)
print(time)
print(car)

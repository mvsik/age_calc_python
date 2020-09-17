#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 20:46:26 2020

@author: kylej
"""

"""

Age Calculator computes the age of an individual given date of birth and current date


"""
import datetime

from dateutil.relativedelta import relativedelta


helpSet = frozenset(["help","-h","--h","-help","--help"])

def printHelp ():
    print("\n")
    print("~~~~~~~~~~~AGE CALCULATOR HELP~~~~~~~~~~~~")
    print("Date should be entered month day year")
    print("month is between 1-12")
    print("day is between 1-31")
    print("year is between 1-9999")
    print("Delimeters accepted are ',' ':' '-' and any whitespace")



dateOfBirthInput = input("Enter Date of Birth month, day, then year: ")

try:
    dateOfBirthInput = dateOfBirthInput.replace(","," ")
    dateOfBirthInput = dateOfBirthInput.replace("-"," ")
    dateOfBirthInput = dateOfBirthInput.replace(":"," ")

except:
    print("\n","Date not recognized. Delimeters accepted are ',' ':' '-' and any whitespace")
    print("typing 'help' will show help instructions")
    raise SystemExit

try:
    month, day, year = dateOfBirthInput.split()
    
except:
    print("\n","Date not recognized. Did you enter enough information?")
    print("typing 'help' will show help instructions")
    raise SystemExit

try:
    dateOfBirth = datetime.date(int(year), int(month), int(day))
    
except ValueError:
    print("\n","Date not recognized. Try month (between 1-12), day(between 1-31), year")
    print("typing 'help' will show help instructions")
    raise SystemExit

print(dateOfBirth)




currentDateInput = input("Enter Current Date month, day, then year: ")

try:
    currentDateInput = currentDateInput.replace(","," ")
    currentDateInput = currentDateInput.replace("-"," ")
    currentDateInput = currentDateInput.replace(":"," ")
except:
    print("\n","Date not recognized. Delimeters accepted are ',' ':' '-' and any whitespace")
    print("typing 'help' will show help instructions")
    raise SystemExit  

try:
    month, day, year = currentDateInput.split()
except:
    print("\n","Date not recognized. Did you enter enough information?")
    print("typing 'help' will show help instructions")
    raise SystemExit    

try:
    currentDate = datetime.date(int(year), int(month), int(day))
    
except ValueError:
    print("\n","Date not recognized. Try month (between 1-12), day(between 1-31), year")
    print("typing 'help' will show help instructions")
    raise SystemExit

print(currentDate)

age = currentDate - dateOfBirth
age_days = age.days
age_hours = age.days * 24
age_minutes = age.days * 24 * 60
age_seconds = age.days * 24 * 60 * 60


print("\nThey are:")
print("Days:",f'{age_days:,}')
print("Hours:",f'{age_hours:,}')
print("Minutes:",f'{age_minutes:,}')
print("Seconds:", f'{age_seconds:,}')
print("Old",'\n')



age_diff = relativedelta(currentDate,dateOfBirth)
print(f'They are {age_diff.years} years, {age_diff.months} months, and {age_diff.days} days old.')















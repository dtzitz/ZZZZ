#Python 
import datetime
import re

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#tool only works for lettered editions
EDITION_REG = re.compile('[a-zA-Z]')
DATE_REG = re.compile('[0-9]{8}')
year = 2020
month = 1
day = 1

# known_edition = input("Please type the edition with the known effective date: ")
# known_date = input('Please type in the effective date for edition {0} using the format YYYYMMDD: '.format(known_edition))

# print(known_edition)
# print(known_date)

def user_input():
    print("NOTE: This program currently only supports character editions ex. AA AB ect")
    known_edition = input("Please type the edition with the known effective date: ")
    if EDITION_REG.match(known_edition) != None:
        pass
    else:
        user_input()

    known_date = input('Please type in the effective date for edition {0} using the format YYYYMMDD: '.format(known_edition))
    if DATE_REG.match(known_date) != None:
        year = int(known_date[:4])
        month = int(known_date[4:6])
        day = int(known_date[6:])
        print('Year is {0} Month is {1} Day is {2}'.format(year, month, day))
    else:
        user_input()

def main():
    user_input()
    

if __name__ == '__main__':
    main()

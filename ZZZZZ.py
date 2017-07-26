#Python 
import datetime
import re

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ALPHABET = [0,26,52,78]
#tool only works for lettered editions
EDITION_REG = re.compile('[a-zA-Z]')
DATE_REG = re.compile('[0-9]{8}')
known_edition = 'BC'
known_edition_value = []
known_edition_point = 0
unknown_edition = 'Z'
year = 2020
month = 1
day = 1
super_rate = '1 year'


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

def count_letters():
    global known_edition_point
    known_edition_reverse = known_edition[::-1]
    for i in range(len(known_edition_reverse)):
        num = LETTERS.find(known_edition_reverse[i])
        known_edition_point += num + ALPHABET[i] #math is wrong
        print(known_edition_point)
    # for letter in known_edition_reverse:
    #     #add the values to the known_edition_value array then math them later?
    #     num = LETTERS.find(letter)
    #     known_edition_value.append(num)
    



def main():
    # user_input()
    count_letters()
    

if __name__ == '__main__':
    main()

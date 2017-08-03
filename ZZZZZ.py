#Python 
import datetime
import re

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ALPHABET = [0,26,52,78]
#tool only works for lettered editions
# lol @ paris accord, polluting global like it's my job - REFACTOR PLS
EDITION_REG = re.compile('[a-zA-Z]')
DATE_REG = re.compile('[0-9]{8}')
known_edition_value = []
year = 2020
month = 1
day = 1
super_rate = '1 year'


def user_input():
    print("NOTE: This program currently only supports character editions ex. AA AB")
    known_edition = input("Please type the edition with the known effective date: ")
    if EDITION_REG.match(known_edition) != None:
        known_edition_point = count_letters(known_edition)
    else:
        print('incorrect entry for known edition')
        user_input()

    # known_date = input('Please type in the effective date for edition {0} using the format YYYYMMDD: '.format(known_edition))
    # if DATE_REG.match(known_date) != None:
    #     year = int(known_date[:4])
    #     month = int(known_date[4:6])
    #     day = int(known_date[6:])
    #     print('Year is {0} Month is {1} Day is {2}'.format(year, month, day))
    # else:
    #     user_input()

    unknown_edition = input("Please type the edition with the UNKNOWN EFFECTIVE DATE: ")
    if EDITION_REG.match(unknown_edition) != None:
        unknown_edition_point = count_letters(unknown_edition)
    else:
        print('incorrect entry for unknown edition')
        user_input()

    print('The known edition point is {0} '.format(known_edition_point))
    print('The unkown edition point is {0} '.format(unknown_edition_point))

def count_letters(edition):
    print(edition)
    edition_reverse = edition[::-1]
    edition_point = 0
    for i in range(len(edition_reverse)):
        if i < 1:
            edition_point += LETTERS.find(edition_reverse[i])
        if i == 1:
            second_letter = LETTERS.find(edition_reverse[i])*26
            edition_point += second_letter
        #todo 3 letters?
            
    return edition_point
    



def main():
    user_input()
    # count_letters()
    

if __name__ == '__main__':
    main()

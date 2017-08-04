#Python 
import datetime
from datetime import timedelta
import re

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#tool only works for lettered editions
# lol @ paris accord, polluting global like it's my job - REFACTOR PLS
EDITION_REG = re.compile('[a-zA-Z]')
DATE_REG = re.compile('[0-9]{8}')
# known_edition_value = []
# super_rate = '1 year'


def user_input():
    print("NOTE: This program currently only supports character editions ex. AA AB")
    known_edition = input("Please type the edition with the known effective date: ")
    if EDITION_REG.match(known_edition) != None:
        known_edition_point = count_letters(known_edition)
    else:
        print('incorrect entry for known edition')
        user_input()

    known_date = input('Please type in the effective date for edition {0} using the format YYYYMMDD: '.format(known_edition))
    if DATE_REG.match(known_date) != None:
        year = int(known_date[:4])
        month = int(known_date[4:6])
        day = int(known_date[6:])
        known_date = datetime.date(year, month, day)
        print('The known date is {0} '.format(known_date))
        year = timedelta(days=365)
        s = known_date - year
        print('some other date is {0} '.format(s))
    else:
        print('you goofed up the date')
        user_input()

    #todo: get supersession rate
    super_rate = input('Please type in the supersession rate using num time (1 day, 1 week, 1 month, 6 months, 1 year')

    unknown_edition = input("Please type the edition with the UNKNOWN EFFECTIVE DATE: ")
    if EDITION_REG.match(unknown_edition) != None:
        unknown_edition_point = count_letters(unknown_edition)
    else:
        print('incorrect entry for unknown edition')
        user_input()

    edition_delta = known_edition_point - unknown_edition_point



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

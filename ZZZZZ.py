#Python 
import datetime
from datetime import timedelta
import re
from dateutil.relativedelta import relativedelta

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#tool only works for lettered editions
EDITION_REG = re.compile('[a-zA-Z]')
DATE_REG = re.compile('[0-9]{8}')


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
    else:
        print('you goofed up the date')
        user_input()

    super_rate = input('Please type in the supersession rate using num time (1 days, 1 weeks, 1 months, 6 months, 1 years :')
    rate_unit = int(super_rate[0])
    duration_string = super_rate[2:]

    unknown_edition = input("Please type the edition with the UNKNOWN EFFECTIVE DATE: ")
    if EDITION_REG.match(unknown_edition) != None:
        unknown_edition_point = count_letters(unknown_edition)
    else:
        print('incorrect entry for unknown edition')
        user_input()

    edition_delta = known_edition_point - unknown_edition_point

    find_date(rate_unit,duration_string,edition_delta,known_date)

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
    
def find_date(rate_unit,duration_string,edition_delta,known_date):
    # six_months = date.today() + relativedelta(months=+6)
    
    rate_unit = rate_unit*edition_delta

    if duration_string == 'months':
        effective_date = known_date - relativedelta(months=+rate_unit)

    if duration_string == 'days':
        effective_date = known_date - relativedelta(days=+rate_unit)

    if duration_string == 'weeks':
        effective_date = known_date - relativedelta(weeks=+rate_unit)

    if duration_string == 'years':
        effective_date = known_date - relativedelta(years=+rate_unit)

    print('The effective date of the unknown edition is {0} '.format(effective_date))
    



def main():
    user_input()
    
    

if __name__ == '__main__':
    main()

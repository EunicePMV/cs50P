def convert_date(month, date, year):
    print(f'{year}-{int(month):02}-{int(date):02}')

MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

done = False
while not done:
    try:
        user_date = input('Date: ').strip()
        month, date, year = user_date.split('/')
        convert_date(month, date, year)
        done = True
    except ValueError:
        try:
            # check with the other format: September 23, 2001
            month, date, year = user_date.split(' ')
            date = date.replace(',', '')

            # check the date if <= 31
            if int(date) > 31:
                continue
            month = str(MONTHS.index(month)+1)
            month = month.strip()
            convert_date(month, date, year)
            done = True
        except ValueError:
            continue



# :( input of 23/6/1912 results in reprompt
#     expected program to reject input, but it did not

# :( input of 1/50/2000 results in reprompt
#     expected program to reject input, but it did not

# :( input of September 8 1636 results in reprompt
#     expected program to reject input, but it did not

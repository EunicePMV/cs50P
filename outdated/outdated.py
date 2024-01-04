def convert_date(month, date, year):
    print(f'{year}-{month}-{date}')



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
        user_date = input('Date: ')
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
            convert(MONTHS.index(month)+1, date, year)
            done = False
        except ValueError:
            continue

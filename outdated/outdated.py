month = [
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

# if invalid date, prompt again:
# 8 September 1636
#

done = False
while not done:
    try:
        user_date = input('Date: ')
        
    except ValueError:
        continue

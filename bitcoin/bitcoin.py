import requests, sys

try:
    ...
except requests.RequestException:
    ...
except IndexError:
    sys.exit('Missing command-line argument')


# command-line argument the number of Bitcoins n
    # convert to float, if not sys.exit
# query the current price of bitcoin as a float
# cost of n bitcoins in USD to four decimal palce using ,

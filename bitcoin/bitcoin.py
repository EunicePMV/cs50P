import requests, sys

try:
    bitcoins = float(sys.argv[1])
except requests.RequestException:
    ...
except IndexError:
    sys.exit('Missing command-line argument')
except ValueError:
    sys.exit('Command-line argument is not a number')


# command-line argument the number of Bitcoins n
    # convert to float, if not sys.exit
# query the current price of bitcoin as a float
# cost of n bitcoins in USD to four decimal palce using ,

import requests, sys, json

try:
    bitcoins = float(sys.argv[1])
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    bitcoin_json = response.json()
    current_price = bitcoin_json['bpi']['USD']['rate']
    print(int(current_price))
    # total = current_price * bitcoins
    # print(f'${total:.4d}')
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

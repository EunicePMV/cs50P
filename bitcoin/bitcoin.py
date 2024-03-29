import requests, sys, json

try:
    bitcoins = float(sys.argv[1])
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    bitcoin_json = response.json()
    current_price = float(bitcoin_json['bpi']['USD']['rate'].replace(',', ''))
    total = current_price * bitcoins
    print(f'${total:,.4f}')
except requests.RequestException:
    ...
except IndexError:
    sys.exit('Missing command-line argument')
except ValueError:
    sys.exit('Command-line argument is not a number')

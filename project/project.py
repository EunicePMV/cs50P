import json, datetime
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

def main():
    customer = []
    customer_name = input('Customer Name: ').strip()
    customer.append(customer_name)

    address = input('Address: ').strip()
    customer.append(address)

    products = []
    num_orders = int(input('Number of Orders: '))
    for _ in range(num_orders):
        item = []
        product = input('Product Name: ').strip()
        quantity = input('Quantity: ').strip()
        price = input('Cost: ').strip()
        item.append(product)
        item.append(quantity)
        item.append(price)
        products.append(item)

    order_data = organize_data(customer, products)
    issued_date, due_date = get_date()
    order_data['issued'] = issued_date
    order_data['due'] = due_date

    total = get_total(order_data)
    order_data['total'] = total
    print(order_data)

    order_json = json.dumps(order_data)

    # Generate invoice
    string_fmt = str(order_json)
    data = json.loads(string_fmt)
    env = Environment(loader=FileSystemLoader('./templates'))
    template = env.get_template('invoice_template.html')
    rendered_template = template.render(data=data)

    with open('rendered.html', 'w') as f:
        f.write(rendered_template)

    HTML('rendered.html').write_pdf('invoice.pdf')

def organize_data(customer, products):
    customer_order = dict()

    customer_order['name'] = customer[0]
    customer_order['address'] = customer[1]

    prod_order = []
    for item in products:
        item_prod = dict()
        item_prod['name'] = item[0]
        item_prod['quantity'] = item[1]
        item_prod['price'] = item[2]
        prod_order.append(item_prod)
    customer_order['product'] = prod_order
    return customer_order


def get_date(issued=None):
    if issued is None:
        current_date = datetime.datetime.now()
    else:
        current_date = datetime.datetime.strptime(issued, "%Y-%m-%d")
    issued_date = current_date.strftime('%B') + " " + "%d, %d" % (current_date.day, current_date.year)

    due_month = current_date.month + 3
    if due_month > 12:
        due_month -= 12
        object_month = datetime.datetime.strptime(str(due_month), '%m')
        due_month = object_month.strftime('%B')
        due_year = current_date.year + 1
        due_date = due_month + ' %d, %d' % (current_date.day, due_year)
    else:
        object_month = datetime.datetime.strptime(str(due_month), '%m')
        due_month = object_month.strftime('%B')
        due_date = due_month + ' %d, %d' % (current_date.day, current_date.year)

    return issued_date, due_date


def get_total(order):
    total = 0
    for item in order['product']:
        total += int(item['price']) * int(item['quantity'])
    return total


if __name__ == "__main__":
    main()

W = 'Weapons'
B = 'Blades'
S = 'Shields'
H = 'Helmets'
A = 'Armor'

testing_products = [
    (101, W, 'Arakh of Khal Drogo', 250),
    (315, W, 'Needle, Sword of Arya Stark', 1050),
    (918, S, 'Stark Infantry Shield', 760),
]

testing_recipients = """
Jon Snow <jon@starks.com>,
arya@starks.com   ,
Eddard "Ned" Stark <ned@starks.com>,
sansa@starks.com,
jon@starks.com,
   Arya No Face <arya@starks.com>
"""

def parse_emails(testing_recipients_template):
  testing_recipients_template = testing_recipients_template.split(',')
  recipients = []
  for row in testing_recipients_template:
    row = row.strip()
    if "<" in row:
      row = row[row.index('<') + 1:row.index('>')].strip()
    if row not in recipients:
      recipients.append(row.strip())
  return recipients


def products_function(testing_products):
  products = "\nSome email text...\n"
  for product in testing_products:
    code,category,name,price = product
    products+="* {}: ${}\n  Buy now using code: {}-{}\n".format(name,price,category[0],code)
  products+="Greetings.\n"
  return products
  
expected_output = (
    [
        'jon@starks.com',
        'arya@starks.com',
        'ned@starks.com',
        'sansa@starks.com'
    ],

    """
Some email text...
* Arakh of Khal Drogo: $250
  Buy now using code: W-101
* Needle, Sword of Arya Stark: $1050
  Buy now using code: W-315
* Stark Infantry Shield: $760
  Buy now using code: S-918
Greetings.
""")

def send_email(recipients, products):
    recipients = parse_emails(recipients)
    products = products_function(products)
    results = ((recipients), (products))
    print(results)
    return results
send_email(testing_recipients, testing_products)
assert send_email(testing_recipients, testing_products) == expected_output

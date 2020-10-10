"""
CHARGE 
CONFIRM
REFUND
PAYOUT -> stripe transfers to a merchant the amnt it collected thru processing 
charges for that merchant, up until the point it receives that action

program;
- track the amount each merchant gets thru charge actions
- for each payout action, print the merchant's balance (after each payout action, the merchant's payout balance is reset to 0)
- payout amnt shld only include the confirmed charges
- stripe's fixed processing fee, 2%
- both stripe and card network fees are applied on the original charge amnt
- refund charges amnt isn't included in payout balance, but card network process fee should be deducted


input;
- N card networks
- each next N lines specify one card network along with its processing fee %
- M actions
- each of the next M lines will specify an action (CHARGE,CONFIRM,REFUND,PAYOUT)
"""

"""
actions;
CHARGE: /charge?network=card_network&amount=amount&merchant_id=merchant_id&charge_id=charge_id
network -> string
amount -> int
merchant_id -> string
charge_id -> string


output;
- list of merchants and payouts. (list of tuples), payouts are rounded up ints
"""
from urllib.parse import parse_qsl, urlparse
from collections import defaultdict
def url_parsers(url):
    components = urlparse(url)
    action, params = components.path, dict(parse_qsl(components.query))
    return action,params

def main(networks,urls): 
    """
    network: list of network type,percentages. ie list of tuples
    urls: list of all url strings
    """
    d = defaultdict(dict) #merchant and all its customers
    possible_payout = 0
    res = []
    for url in urls:
        action, params = url_parsers(url)

        if action == "/charge":
            merchant_id, charge_id, network = params["merchant_id"], params["charge_id"], params["network"]
            possible_payout = int(params["amount"])
            d[merchant_id][charge_id] = [possible_payout,network]
            print(d)

        if action == "/confirm":
            charge_id = params["charge_id"]
            d[merchant_id][charge_id][0] -= ((networks[d[merchant_id][charge_id][1]]+2)/100) * d[merchant_id][charge_id][0]

        if action == "/refund":
            charge_id = params["charge_id"]
            d[merchant_id][charge_id][0] *= -(networks[d[merchant_id][charge_id][1]]/100)

        if action == "/payout":
            merchant_id = params["merchant_id"]
            total_sum = sum(val[0] for key,val in d[merchant_id].items())
            res.append((merchant_id,round(total_sum)))
            for id_ in d[merchant_id]:
                d[merchant_id][id_][0] = 0 

    return res 

networks = {"visa":2.0,"mastercard":3}
urls = ["2","visa 2.0", "mastercard 3.0", "8",
        "/charge?merchant_id=m001&charge_id=c001&amount=1000&network=mastercard",
        "/charge?merchant_id=m001&charge_id=c002&amount=1000&network=visa",
        "/confirm?charge_id=c001",
        "/confirm?charge_id=c002",
        "/payout?merchant_id=m001",
        "/charge?merchant_id=m001&charge_id=c003&amount=1000&network=visa",
        "/confirm?charge_id=c003",
        "/payout?merchant_id=m001"
        ]

# res = main(networks,urls)
# print(res)

#hackerrank format
def process_actions(input_lines):
    #write code here
    from urllib.parse import parse_qsl, urlparse
    from collections import defaultdict
    n = int(input_lines[0])
    networks = {}
    d = defaultdict(dict)

    for i in range(1,n+1):
        temp = input_lines[i].split()
        networks[temp[0]] = float(temp[1])

    for i in range(n+2, len(input_lines)):
        url = input_lines[i]
        components = urlparse(url)
        action, params = components.path, dict(parse_qsl(components.query))
        if "merchant_id" in params:
            merchant_id = params["merchant_id"]
        if "charge_id" in params:
            charge_id = params["charge_id"]
        process_query(networks,action,params,d,merchant_id,charge_id)


def process_query(networks,action,params,d,merchant_id,charge_id):
    if action == "/charge":
        merchant_id, charge_id, network = params["merchant_id"], params["charge_id"], params["network"]
        possible_payout = int(params["amount"])
        d[merchant_id][charge_id] = [possible_payout,network]
        print(d)

    if action == "/confirm":
        charge_id = params["charge_id"]
        d[merchant_id][charge_id][0] -= ((networks[d[merchant_id][charge_id][1]]+2)/100) * d[merchant_id][charge_id][0]

    if action == "/refund":
        charge_id = params["charge_id"]
        d[merchant_id][charge_id][0] *= -(networks[d[merchant_id][charge_id][1]]/100)

    if action == "/payout":
        merchant_id = params["merchant_id"]
        total_sum = sum(val[0] for key,val in d[merchant_id].items())
        print(merchant_id,',',round(total_sum))
        for id_ in d[merchant_id]:
            d[merchant_id][id_][0] = 0

    
res = process_actions(urls)
print(res)
from urllib.parse import parse_qsl, urlparse
from collections import defaultdict
from math import ceil
def process_actions(input_lines):
    # Write your code here
    n = int(input_lines[0])
    networks = {}
    d = defaultdict(dict)
    
    #maping the networks and their charge percentages
    for i in range(1,n+1):
        temp = input_lines[i].split()
        networks[temp[0]] = float(temp[1])
    
    #looping through each url    
    for i in range(n+2,len(input_lines)):
        url = input_lines[i]
        components = urlparse(url)
        action, params = components.path, dict(parse_qsl(components.query))
        if "merchant_id" in params:
            merchant_id = params["merchant_id"]
        if "charge_id" in params:
            charge_id = params["charge_id"]
        #helper function to display payout
        process_query(networks,action,params,d, merchant_id, charge_id)
        
        
def process_query(networks,action,params,d, merchant_id,charge_id):
    if action == "/charge":
        merchant_id, charge_id, network = params["merchant_id"], params["charge_id"], params["network"]
        possible_payout = int(params["amount"])
        d[merchant_id][charge_id] = [possible_payout,network]
        
    if action == "/confirm":
        charge_id = params["charge_id"]
        d[merchant_id][charge_id][0] -= ((networks[d[merchant_id][charge_id][1]]+2)/100) * d[merchant_id][charge_id][0]
        
    if action == "/refund":
        charge_id = params["charge_id"]
        d[merchant_id][charge_id][0] *= -(networks[d[merchant_id][charge_id][1]]/100)
        
    if action == "/payout":
        merchant_id = params["merchant_id"]
        total_sum = sum(val[0] for key,val in d[merchant_id].items())
        print(f"{merchant_id}, {ceil(total_sum)}")
        for id_ in d[merchant_id]:
            d[merchant_id][id_][0] = 0
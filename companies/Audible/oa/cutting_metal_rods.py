def max_profit(cutting_cost, sale_price, rods, cutting_size):
    profit = 0
    total_rods = len(rods)
    for i in range(total_rods):
        if rods[i]%cutting_size == 0:
            profit += (sale_price * rods[i]-(rods[i] // cutting_size-1) * cutting_cost)

        else:
            profit += (sale_price * (rods[i] - rods[i] % cutting_size) - (rods[i] // cutting_size)* cutting_cost)


    return profit

cutting_cost = int(input("Cutting Cost: "))
sale_price = int(input("Sale Price : "))
road_number = int(input("Number of Rods : "))
rods=[]
for i in range(road_number):
    rod = int(input())
    rods.insert(i,rod)

max_size_road = max(rods)
maximum_profit=0
for cutting_size in range(1,max_size_road):
    profit = max_profit(cutting_cost,sale_price,rods,cutting_size)
    
    if profit > maximum_profit:
        maximum_profit=profit

print(maximum_profit) 
def hashMap(queryType, query):
    count = 0
    d = dict()
    for i in range(len(queryType)):
        
        if queryType[i] == "insert":
            insert(query[i][0],query[i][1],d)
        elif queryType[i] == "addToKey":
            add_to_key(query[i][0],d)
        elif queryType[i] == "addToValue":
            add_to_value(query[i][0],d)
            print(queryType[i])
        elif queryType[i] == "get":
            count += d[query[i][0]]
            print(query[i])
    return count
            
def insert(x,y,d):
    d[x] = y
    
def add_to_key(x,d):
    key_val = [(k+x,v) for k,v in d.items()]
    #d = {}
    for i,j in key_val:
        d[i] = j
        
def add_to_value(x,d):
    for key,val in d.items():
        d[key] += x

qtype = ["insert", "insert", "addToValue", "addToKey", "get"]
query = [[1,2], [2,3], [2], [1], [3]]

res = hashMap(qtype,query)
print(res)
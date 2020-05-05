def flattenDictionary(d):
    flattened_dictionary = {}

    def flatten(dic,buks=''):
        for k,v in dic.items():
            if k == '':
                k = bus 
            else:
                if bus != '':
                    k = bus + '.' + k 

            
            if type(v) == dict:
                flatten(v,k)
            else:
                flattened_dictionary[k] = v
            
        
    
    flatten(d)
    return flattened_dictionary


r = flattenDictionary({'key1':'1','key2':{'a':'2','b':'3','c':{'d':'3','c':{'':'1'}}}})
print(r)



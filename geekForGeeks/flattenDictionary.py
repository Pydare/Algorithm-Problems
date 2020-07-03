
def flatten(d):
    output = {}

    for key, value in d.items():
        if isinstance(value,dict):
            ans = flatten(value)
            for k1, v1 in ans.items():
                if k1 != "":
                    output[key + "." + k1] = v1
                else:
                    output[key] = v1
        else:
            output[key] = value 

    return output

p = {"a":1,
    "b":{"c":2, "d":3},
    "e": {"f":{"g":4,"h":5},"i":6},
    "j":{"":7}
    }
res = flatten(p)
print(res) 
def playDic():
    map = dict(tom = "Tom Jack", mike = "Michael Jones")
    map['chris'] = "Chris Chapel"

    map.pop('mike') # remove the key and value
    map['chris'] = None # only remove the value
    for key in sorted(map):
        print(key, map[key], sep=", ")

    map['mike'] = "Mike Cannon-Brooke"
    map['malcon'] = "Malcon Turnbull"
    for v in map.values():
        print(v)


playDic()
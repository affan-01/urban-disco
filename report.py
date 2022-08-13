def remove_none_values(dic):
    items = []
    for key,value in dic.items():
        if value is None:
            items.append(key)
    for key in items:
        del dic[key]
    return dic
           
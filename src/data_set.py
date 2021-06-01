def data_set(data,ab=0):
    # ab가 1이면 절대값
    value = []
    for i in range(0,len(data)):
        value1 = data[i].text.split(',')
        value1 = list(map(float,value1))
        if ab == 0:
            value.append(value1)
        elif ab == 1:
            value2 = list(map(abs,value1))
            value.append(value2)
    return value
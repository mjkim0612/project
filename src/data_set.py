def data_set(data,ab=0):
    # ab가 1이면 절대값
    value = []
    for i in range(0,len(data)):
        y_value1 = data[i].text.split(',')
        y_value1 = list(map(float,y_value1))
        if ab == 0:
            value.append(y_value1)
        elif ab == 1:
            value2 = list(map(abs,y_value1))
            value.append(value2)
    return value
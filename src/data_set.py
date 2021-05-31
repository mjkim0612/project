def data_set(y_data,ab=0):
    # ab가 1이면 절대값
    y_value = []
    for i in range(0,len(y_data)):
        y_value1 = y_data[i].text.split(',')
        y_value1 = list(map(float,y_value1))
        if ab == 0:
            y_value.append(y_value1)
        elif ab == 1:
            y_value2 = list(map(abs,y_value1))
            y_value.append(y_value2)
    return y_value
data_file = open('data.json', 'r')
data = eval(data_file.read())
data_file.close()
d = {}
for elem in data:
    for key in data[elem]:
        if not(d.get(key)):
            d[key] = 1
    else:
        other = [key, d.get(key) + 1]
        d.pop(key)
        d.update([other])

l = [[''] for i in range(1000)]
for key in d:
    a = l[d[key]]
    a.append(key)
    l[d[key]] = a

for i in range (len(l)):
    if (len(l[i]) > 1):
        print('Эти темы встретились', i, 'раз(а):', l[i][1:])


        
               

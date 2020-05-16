#height
people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]
x=list(map(lambda x:x['height'],filter(lambda y:'height' in y ,people)))
if len(x)>0:
    average_height=sum(x)/len(x)

print (average_height)
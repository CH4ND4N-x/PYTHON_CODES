#tempeture
fahrenheit = {'t1':-30, 't2':-20, 't3':-10, 't4':0}
celsius={k:((v-32)/1.8) for (k,v) in fahrenheit.items()} 
print(celsius)
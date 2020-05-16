#map1
import random
names = ['Mary', 'Isla', 'Sam']
names=map(lambda x:random.choice(['Mr. Pink','Mr. Orange','Mr. Blonde']) ,names)
print (list(names))

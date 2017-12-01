from django.test import TestCase

# Create your tests here.


import copy
d = {'1':1, '2':2}
print(id(d))
d2 = copy.deepcopy(d)
# d2 = d
print(id(d))
print(id(d2))
d2['1']=5



print(d['1']+d2['1'])
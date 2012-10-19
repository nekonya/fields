>>> import fields
>>> factory_A = fields.record('A', [ 'a', 'b', 'c' ] )
>>> factory_A
<class 'fields.A'>

>>> container_A = factory_A(1,2,3)
>>> container_A
<a=1, b=2, c=3>

>>> container_A.a == 1 and container_A.b == 2 and container_A.c == 3
True

>>> try:
...     container_A.d = 0
... except AttributeError, e:
...     print(e)
'A' object has no attribute 'd'

>>> fields.namedtuple('B', ['a', 'b', 'c'])
<class 'fields.B'>

>>> fields.dict_to_namedtuple('animal',{'neko':4, 'kame':{'risu':2}, 'kuma':5})
animal(neko=4, kuma=5, kame={'risu': 2})

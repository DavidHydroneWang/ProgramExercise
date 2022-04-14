#!/usr/bin/env python
# coding=utf-8
from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')

tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))

print(tokyo)
print(tokyo[0])
print(tokyo[1])
print(tokyo.population)
print(City._fields)

LatLong = namedtuple('LatLong', 'lat lang')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613389, 77.208889))
delhi = City._make(delhi_data)

print(delhi._asdict())

for key, value in delhi._asdict().items():
    print(key + ':', value)

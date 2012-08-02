# -*- coding: utf-8 -*-

from __future__ import print_function
import collections
from itertools import chain, repeat, izip

def __record(name, fields):
    def __init__(self, *args):
        if len(args) > len(fields):
            raise TypeError("__init__() takes at most %d arguments (%d given)" % (len(fields)+1, len(args)+1))
        args = chain(args, repeat(None))
        for field, value in izip(fields, args):
            setattr(self, field, value)

    def __repr__(self):
        return '<' + ', '.join([ '{0}={1}'.format(x,str(getattr(self,x))) for x in self.__slots__ ]) + '>'

    attrs = dict()
    attrs["__slots__"] = fields
    attrs["__init__"] = __init__
    attrs["__repr__"] = __repr__
    attrs["__str__"] = __repr__
    return type(name, (object,), attrs)

def record(name, fields):
    if isinstance(fields,str):
        return __record(name, fields.split())
    elif isinstance(fields,list):
        return __record(name, fields)
    else:
        raise TypeError('\'a string\' or \'a list of string\' is required\n')

def namedtuple(name, fields):
    if isinstance(fields,str):
        return collections.namedtuple(name, fields)
    elif isinstance(fields,list):
        return collections.namedtuple(name, ' '.join(fields))
    else:
        raise TypeError('\'a string\' or \'a list of string\' is required\n')

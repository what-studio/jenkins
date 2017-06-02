# -*- coding: utf-8 -*-
"""
   jenkins_cffi.build
   ~~~~~~~~~~~~~~~~~~

   Builds ``lookup3.c`` to be used for PyPy.

   :copyright: (c) 2017, What! Studio
   :license: MIT, see LICENSE for more details.

"""
import os

from cffi import FFI


with open(os.path.join(os.path.dirname(__file__), 'lookup3.c')) as f:
    code = f.read()


ffibuilder = FFI()
ffibuilder.set_source('jenkins_cffi._lookup3', code)
ffibuilder.cdef('''
uint32_t hashlittle(const void*, size_t, uint32_t);
void hashlittle2(const void *, size_t, uint32_t*, uint32_t*);
''')


if __name__ == '__main__':
    ffibuilder.compile()

# -*- coding: utf-8 -*-
"""
   jenkins_cffi
   ~~~~~~~~~~~~

   Jenkins hash for PyPy.

   :copyright: (c) 2017, What! Studio
   :license: MIT, see LICENSE for more details.

"""
try:
    from jenkins_cffi._lookup3 import ffi, lib as lookup3
except ImportError:
    ffi = lookup3 = NotImplemented


__all__ = ['hashlittle', 'hashlittle2']


def hashlittle(s, seed=0):
    return lookup3.hashlittle(s, len(s), seed)


def hashlittle2(s, seed1=0, seed2=0):
    init_val1 = ffi.new('uint32_t*')
    init_val2 = ffi.new('uint32_t*')
    lookup3.hashlittle2(s, len(s), init_val1, init_val2)
    return init_val1[0], init_val2[0]

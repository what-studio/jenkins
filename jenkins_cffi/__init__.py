# -*- coding: utf-8 -*-
"""
   jenkins_cffi
   ~~~~~~~~~~~~

   Jenkins hash for PyPy.

   :copyright: (c) 2017, What! Studio
   :license: MIT, see LICENSE for more details.

"""
try:
    import jenkins_cffi._lookup3.lib as lookup3
except ImportError:
    lookup3 = NotImplemented


__all__ = ['hashlittle', 'hashlittle2']


def hashlittle(s, seed=0):
    return lookup3.hashlittle(s, len(s), seed)


def hashlittle2(s, seed1=0, seed2=0):
    init_val1 = c_int(seed1)
    init_val2 = c_int(seed2)
    lookup3.hashlittle2(s, len(s), byref(init_val1), byref(init_val2))
    return init_val1.value, init_val2.value

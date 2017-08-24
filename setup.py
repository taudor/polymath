# This is the setup file for the polymathmodule.c extension

from distutils.core import setup, Extension
import numpy

polymath = Extension('polymath',
                    include_dirs=['/usr/local/include', numpy.get_include() + '/numpy'],
                                  # '/usr/local/Cellar/numpy/1.13.1/lib/python2.7/site-packages/numpy/core/include/numpy',
                                  # '/usr/local/Cellar/numpy/1.13.1_1/lib/python3.6/site-packages/numpy/core/include/numpy'],
                    sources=['./polymath_src/python_wrapper.c',
                             './polymath_src/polymath_c/poly_array_to_uint64.c',
                             './polymath_src/polymath_c/uint64_to_poly_array.c',
                             './polymath_src/polymath_c/shift_lfsr.c',
                             './polymath_src/polymath_c/polynomial_multiplication.c',
                             './polymath_src/polymath_c/polynomial_modulo_padding.c'])

setup(name='polymath',
      version='0.1',
      description='Lightweight and fast implementation of polynomial operations over GF(2).',
      ext_modules=[polymath])

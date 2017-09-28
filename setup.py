# This is the setup file for the polymathmodule.c extension

from setuptools import setup
from setuptools.extension import Extension

import numpy

polymath = Extension('polymath',
                    include_dirs=[#'/usr/local/include', '/usr/include', numpy.get_include() + '/numpy', 
                    numpy.get_include(), './polymath_src/polymath_c'],
                                  # '/usr/local/Cellar/numpy/1.13.1/lib/python2.7/site-packages/numpy/core/include/numpy',
                                  # '/usr/local/Cellar/numpy/1.13.1_1/lib/python3.6/site-packages/numpy/core/include/numpy'],
                    sources=['polymath_src/python_wrapper.c',
                             'polymath_src/polymath_c/poly_array_to_uint64.c',
                             'polymath_src/polymath_c/uint64_to_poly_array.c',
                             'polymath_src/polymath_c/shift_lfsr.c',
                             'polymath_src/polymath_c/polynomial_multiplication.c',
                             'polymath_src/polymath_c/polynomial_modulo_padding.c',
                             'polymath_src/polymath_c/polynomial_modulo.c',
                             'polymath_src/polymath_c/dot.c',
                             'polymath_src/polymath_c/eval_id_xor.c',
                             ],
                     )

setup(name='polymath',
      packages=['polymath_src'],
      version='0.1.16',
      description='Lightweight and fast implementation of polynomial operations over GF(2).',
      author='Tudor Soroceanu',
      author_email='tudor200@zedat.fu-berlin.de',
      url='https://github.com/taudor/polymath',
      download_url='https://github.com/taudor/polymath/archive/0.1.16.tar.gz',
      keywords=['polynomials','LFSR','GF(2)'],
      classifiers = [],
      setup_requires = ['numpy'],
      install_requires = ['numpy'],
      ext_modules=[polymath])

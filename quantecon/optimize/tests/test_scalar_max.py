"""
Tests for scalar maximization.

"""
import numpy as np
from numpy.testing import assert_almost_equal
from numba import njit

from quantecon.optimize import brent_max

@njit
def f(x):
    """
    A function for testing on.
    """
    return -(x + 2.0)**2 + 1.0

def test_brent_max():
    """
    Uses the function f defined above to test the scalar maximization 
    routine.
    """
    true_fval = 1.0
    true_xf = -2.0
    xf, fval, info = brent_max(f, -2, 2)
    assert_almost_equal(true_fval, fval, decimal=4)
    assert_almost_equal(true_xf, xf, decimal=4)
    
@njit
def g(x, y):
    """
    A multivariate function for testing on.
    """
    return -x**2 + y
    
def test_brent_max():
    """
    Uses the function f defined above to test the scalar maximization 
    routine.
    """
    y = 5
    true_fval = 5.0
    true_xf = -0.0
    xf, fval, info = brent_max(g, -10, 10, args=(y,))
    assert_almost_equal(true_fval, fval, decimal=4)
    assert_almost_equal(true_xf, xf, decimal=4)


if __name__ == '__main__':
    import sys
    import nose

    argv = sys.argv[:]
    argv.append('--verbose')
    argv.append('--nocapture')
    nose.main(argv=argv, defaultTest=__file__)



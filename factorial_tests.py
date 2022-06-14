##################################################
## Contains the tests of the factorial module
## This file is optional, but unit testing
## is always a bonus
##################################################

from factorial import factorial 

def test_factorial():
    assert factorial('3') == 6.0
    assert factorial('0') == 1.0
    assert factorial('1') == 1.0
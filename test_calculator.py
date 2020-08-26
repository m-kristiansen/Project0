from calculator import add, factorial, sin, divition, times, power
import numpy as np
import math
import pytest

def test_add_exercise_1():
    x = 1
    y = 1
    computed = add(x,y)
    expected = 3
    assert computed == expected, 'Addition of integers doesnt work'

def test_floating_add_exercise_2():
    x = 0.1
    y = 0.2
    computed = add(x, y)
    expected = 0.3
    tol = 1e-12
    assert np.abs(computed - expected) <= tol, 'Addition of floating numbers doesnt work'

def test_string_add_exercise_3():
    x = 'Hello '
    y = 'World'
    computed = add(x, y)
    expected = 'Hello World'
    assert expected == computed, 'Addition of strings doesnt work'

def test_factorial_exercise_4():
    x = 5
    expected = math.factorial(x)
    computed = factorial(x)
    assert expected == computed, 'factorial of 5 doesnt work'

def test_sin_exercise_4():
     x = np.pi/2
     expected = np.sin(x)
     computed = sin(x)
     tol = 1e-6
     assert abs(expected - computed)< tol, 'sin of pi/2 doesnt work'


def test_divition_exercise_4():
    x = 3
    y = 2
    expected = 1.5
    computed = divition(3,2)
    assert computed == expected, 'the divition 3/2 doesnt work'


def test_times_exercise_4():
    x = 3
    y = 2
    expected = 6
    computed = times(3,2)
    assert computed == expected, 'the multiplication 3*2 doesnt work'

def test_power_exercise_4():
    x = 3
    y = 2
    expected = 3**2
    computed = power(3, 2)
    tol = 1e-6
    assert abs(computed - expected)< tol, 'the calculation of 3**2 doesnt work'


def test_add_exeption_exercise_5():
    with pytest.raises(TypeError):
        add("Hello", 3)

def test_divition_exeption_exercise_5():
    with pytest.raises(ZeroDivisionError):
        divition(2, 0)



@pytest.mark.parametrize("arg, expected_output", [[(1,1), 2], [(3,4),7]
, [(3, 23), 26]])
def test_add_exercise_6(arg, expected_output):
    assert add(arg[0], arg[1]) == expected_output

@pytest.mark.parametrize("arg, expected_output", [[(0.1,0.2), 0.3], [(0.0,0.1), 0.1],
[(0.69,0.69), 1.38]])
def test_floating_add_exercise_6(arg, expected_output):
    computed = add(arg[0], arg[1])
    tol = 1e-6
    assert abs(computed-expected_output) < tol

@pytest.mark.parametrize("arg, expected_output", [[("h", "p"), "hp"], [("hey ", "you"),
"hey you"], [("2", "4"), "24"]])
def test_string_add_exercise_6(arg, expected_output):
    assert add(arg[0], arg[1]) == expected_output


@pytest.mark.parametrize("arg, expected_output", [[6, math.factorial(6)], [4,
math.factorial(4)], [12, math.factorial(12)]])
def test_factorial_exercise_6(arg, expected_output):
    assert factorial(arg) == expected_output


@pytest.mark.parametrize("arg, expected_output", [[np.pi, np.sin(np.pi)],
[np.pi/8, np.sin(np.pi/8)], [0.134, np.sin(0.134)]])
def test_sin_exercise_6(arg, expected_output):
    computed = sin(arg)
    tol =1e-6
    assert abs(computed-expected_output) < tol

@pytest.mark.parametrize("arg, expected_output", [[(0.2, 0.1), 2], [(4,2), 2],
[(3, 6), 0.5]])
def test_divition_exercise_6(arg, expected_output):
    assert divition(arg[0], arg[1]) == expected_output

@pytest.mark.parametrize("arg, expected_output", [[(0.2, 0.1), 0.02], [(4,2), 8],
[(3, 6), 18]])
def test_times_exercise_6(arg, expected_output):
    computed = times(arg[0], arg[1])
    tol = 1e-6
    assert abs(computed - expected_output) < tol

@pytest.mark.parametrize("arg, expected_output", [[(2,4), 16], [(0.3, 0.2), 0.786],
 [(1, 2), 1]])
def test_power_exercise_6(arg, expected_output):
    computed = power(arg[0], arg[1])
    tol = 1e-4
    assert abs(computed-expected_output) < tol

@pytest.mark.parametrize("arg, expected_output", [[("s", 2), TypeError], [(2, "1"),
TypeError], [(0.2, "1"), TypeError]])
def test_add_exeption_exercise_6(arg, expected_output):
    with pytest.raises(expected_output):
        add(arg[0], arg[1])

@pytest.mark.parametrize("arg, expected_output", [[("s", 2), TypeError], [(2, 0),
ZeroDivisionError], [(0.2, 0), ZeroDivisionError]])
def test_add_exeption_exercise_6(arg, expected_output):
    with pytest.raises(expected_output):
        divition(arg[0], arg[1])

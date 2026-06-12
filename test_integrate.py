import math
import pytest


def integrate(f, a, b, n=1000):
    h = (b - a) / n
    s = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        s += f(a + i * h)
    return s * h


def test_integrate_constant():
    # Known ground truth: integral of 1 over [0,1] is exactly 1.0
    assert integrate(lambda x: 1, 0, 1, n=1000) == pytest.approx(1.0)


def test_plausibility_sin():
    # Plausibility: integral of sin over [0, pi/2] should be between 0 and 1
    res = integrate(math.sin, 0, math.pi / 2, n=1000)
    assert 0 < res < 1


@pytest.mark.parametrize("n", [10, 100, 1000])
def test_integrate_x(n):
    # Parametrized: integral of x over [0,1] is 0.5 (exact for the trapezoid rule)
    assert integrate(lambda x: x, 0, 1, n=n) == pytest.approx(0.5)

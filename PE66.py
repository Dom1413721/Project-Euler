

from sympy.ntheory.primetest import is_square
from sympy.solvers.diophantine.diophantine import diop_DN


def A002350(n): return 1 if is_square(n) else next(a for a, b in diop_DN(n, 1))

print(max(A002350[0:1000]))
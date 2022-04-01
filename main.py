# Problem 39:
#     Integer Right Triangles
#
# Description:
#     If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
#       there are exactly three solutions for p = 120.
#
#         { 20, 48, 52 },
#         { 24, 45, 51 },
#         { 30, 40, 50 }
#
#     For which value of p ≤ 1000, is the number of solutions maximised?

from collections import defaultdict
from math import sqrt


def main(n):
    """
    Returns the perimeter `p` (≤ `n`) for which
      the number of integer right triangles is maximized.,
      as well as a list of the triangles for `p`.

    Args:
        n (int): Natural number, at least 12

    Returns:
        (Tuple[int, List[Tuple[int, int, int]]]):
            Tuple of...
              * Perimeter `p` (≤ `n`) having max number of integer right triangles
              * List of triangles by sides (a,b,c)
    """
    assert type(n) == int and n >= 12

    # Keep track of known triangles
    triangles = defaultdict(lambda: [])

    # Iterate through all possible combinations of sides {a,b,c}.
    # Smallest possible triangle is {3,4,5} = 12, so start there.
    for p in range(12, n+1):
        for a in range(3, p//3):
            for b in range(a+1, (p-a)//2):
                c = p - a - b
                if sqrt(a**2 + b**2) == c:
                    triangles[p].append((a, b, c))

    # Search for best perimeter
    p_best = None
    p_count = 0
    for p in triangles:
        if len(triangles[p]) > p_count:
            p_best = p
            p_count = len(triangles[p])

    return p_best, triangles[p_best]


if __name__ == '__main__':
    num = int(input('Enter a natural number (at least 12): '))
    perimeter, sols = main(num)
    print('Perimeter p (≤ {}) having maximum number of integer right triangles:'.format(num))
    print('  p = {} has {} triangles'.format(perimeter, len(sols)))
    print('Triangles:')
    for sol in sols:
        print('    [ {:8d}, {:8d}, {:8d} ]'.format(*sol))

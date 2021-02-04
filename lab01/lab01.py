import unittest
import sys
from contextlib import contextmanager
from io import StringIO

#################################################################################
# TESTING OUTPUTS
#################################################################################
@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

#################################################################################
# EXERCISE 1
#################################################################################

# implement this function
def is_perfect(n):
    allDivisors=0
    divisor=1
    if(n<0):
        return False
    while(divisor<n):
        if(n%divisor==0):
            allDivisors+=divisor
        divisor+=1
    return allDivisors==n

# (3 points)
def test1():
    tc = unittest.TestCase()
    for n in (6, 28, 496):
        tc.assertTrue(is_perfect(n), '{} should be perfect'.format(n))
    for n in (1, 2, 3, 4, 5, 10, 20):
        tc.assertFalse(is_perfect(n), '{} should not be perfect'.format(n))
    for n in range(30, 450):
        tc.assertFalse(is_perfect(n), '{} should not be perfect'.format(n))

#################################################################################
# EXERCISE 2
#################################################################################

# implement this function
def multiples_of_3_and_5(n):
    count=0
    for i in range(n):
        if(i%3==0 or i%5==0):
            count+=i
    return count

# (3 points)
def test2():
    tc = unittest.TestCase()
    tc.assertEqual(multiples_of_3_and_5(10), 23)
    tc.assertEqual(multiples_of_3_and_5(500), 57918)
    tc.assertEqual(multiples_of_3_and_5(1000), 233168)

#################################################################################
# EXERCISE 3
#################################################################################
def integer_right_triangles(p):
    numTrips=0
    s1=1
    s2=0
    s3=0
    while(s1<p):
        s2=s1
        while(s2<p):
            s3=s2
            while(s3<p):
                if(((s1**2+s2**2==s3**2) or (s1**2+s3**2==s2**2) or (s2**2+s3**2==s1**2)) and (s1+s2>s3 and s1+s3>s2 and s2+s3>s1) and (s1+s2+s3==p)):
                    numTrips+=1
                s3+=1
            s2+=1
        s1+=1
    return numTrips

def test3():
    tc = unittest.TestCase()
    tc.assertEqual(integer_right_triangles(60), 2)
    tc.assertEqual(integer_right_triangles(100), 0)
    tc.assertEqual(integer_right_triangles(180), 3)

#################################################################################
# EXERCISE 4
#################################################################################

# implement this function
def gen_pattern(chars):
    length=len(chars)
    char=chars
    charRev=chars[::-1]
    bottom=[]
    index=1
    while(index<length+1):
        temp=charRev[0:index]+char[length-index+1:length]
        temp='.'.join(temp)
        temp=temp.center((length*4)-3,".")
        bottom.append(temp)
        print(temp)
        index+=1
    for i in range(2, length+1):
        print(bottom[-i])
    
    pass

def test4():
    tc = unittest.TestCase()
    with captured_output() as (out,err):
        gen_pattern('@')
        tc.assertEqual(out.getvalue().strip(), '@')
    with captured_output() as (out,err):
        gen_pattern('@%')
        tc.assertEqual(out.getvalue().strip(),
        """
..%..
%.@.%
..%..
""".strip())
    with captured_output() as (out,err):
        gen_pattern('ABC')
        tc.assertEqual(out.getvalue().strip(),
        """
....C....
..C.B.C..
C.B.A.B.C
..C.B.C..
....C....
""".strip())
    with captured_output() as (out,err):
        gen_pattern('#####')
        tc.assertEqual(out.getvalue().strip(),
                             """
........#........
......#.#.#......
....#.#.#.#.#....
..#.#.#.#.#.#.#..
#.#.#.#.#.#.#.#.#
..#.#.#.#.#.#.#..
....#.#.#.#.#....
......#.#.#......
........#........
""".strip())
    with captured_output() as (out,err):
        gen_pattern('abcdefghijklmnop')
        tc.assertEqual(out.getvalue().strip(),
"""
..............................p..............................
............................p.o.p............................
..........................p.o.n.o.p..........................
........................p.o.n.m.n.o.p........................
......................p.o.n.m.l.m.n.o.p......................
....................p.o.n.m.l.k.l.m.n.o.p....................
..................p.o.n.m.l.k.j.k.l.m.n.o.p..................
................p.o.n.m.l.k.j.i.j.k.l.m.n.o.p................
..............p.o.n.m.l.k.j.i.h.i.j.k.l.m.n.o.p..............
............p.o.n.m.l.k.j.i.h.g.h.i.j.k.l.m.n.o.p............
..........p.o.n.m.l.k.j.i.h.g.f.g.h.i.j.k.l.m.n.o.p..........
........p.o.n.m.l.k.j.i.h.g.f.e.f.g.h.i.j.k.l.m.n.o.p........
......p.o.n.m.l.k.j.i.h.g.f.e.d.e.f.g.h.i.j.k.l.m.n.o.p......
....p.o.n.m.l.k.j.i.h.g.f.e.d.c.d.e.f.g.h.i.j.k.l.m.n.o.p....
..p.o.n.m.l.k.j.i.h.g.f.e.d.c.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p..
p.o.n.m.l.k.j.i.h.g.f.e.d.c.b.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p
..p.o.n.m.l.k.j.i.h.g.f.e.d.c.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p..
....p.o.n.m.l.k.j.i.h.g.f.e.d.c.d.e.f.g.h.i.j.k.l.m.n.o.p....
......p.o.n.m.l.k.j.i.h.g.f.e.d.e.f.g.h.i.j.k.l.m.n.o.p......
........p.o.n.m.l.k.j.i.h.g.f.e.f.g.h.i.j.k.l.m.n.o.p........
..........p.o.n.m.l.k.j.i.h.g.f.g.h.i.j.k.l.m.n.o.p..........
............p.o.n.m.l.k.j.i.h.g.h.i.j.k.l.m.n.o.p............
..............p.o.n.m.l.k.j.i.h.i.j.k.l.m.n.o.p..............
................p.o.n.m.l.k.j.i.j.k.l.m.n.o.p................
..................p.o.n.m.l.k.j.k.l.m.n.o.p..................
....................p.o.n.m.l.k.l.m.n.o.p....................
......................p.o.n.m.l.m.n.o.p......................
........................p.o.n.m.n.o.p........................
..........................p.o.n.o.p..........................
............................p.o.p............................
..............................p..............................
""".strip()
)

#################################################################################
# RUN ALL TESTS
#################################################################################
def main():
    test1()
    test2()
    test3()
    test4()

if __name__ == '__main__':
    main()

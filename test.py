from z3 import *

s = Solver()
x1, x2 = Reals("x1 x2")
w1_1_1, w1_2_1, b1_1 = Reals("w1_1_1 w1_2_1 b1_1")
w1_1_2, w1_2_2, b1_2 = Reals("w1_1_2 w1_2_2 b1_2")
w2_1, w2_2, b2 = Reals("w2_1 w2_2 b2")
g1_1, g1_2, g = Reals("g1_1 g1_2 g")
f1_1, f1_2, f2 = Reals("f1_1 f1_2 f2")


s.add(w1_1_1 == 3.4243)
s.add(w1_2_1 == 3.4299)
s.add(b1_1 == -5.3119)

s.add(w1_1_2 == 4.4863)
s.add(w1_2_2 == 4.4830)
s.add(b1_2 == -1.7982)

s.add(w2_1 == -7.1722)
s.add(w2_2 == 6.7997)
s.add(b2 == -3.0611)
s.add(g1_1 == w1_1_1*x1 + w1_2_1*x2 + b1_1)
s.add(g1_2 == w1_1_2*x1 + w1_2_2*x2 + b1_2)

s.add(f1_1 == 1/(1+2.718**(-1*g1_1)))
s.add(f1_2 == 1/(1+2.718**(-1*g1_2)))
s.add(g == w2_1*f1_1 + w2_2*f1_2 + b2)
s.add(f2 == 1/(1+2.718**(-1*g)))

s.add(And(
    Or(Not(And(x1 < 0.5, x2 < 0.5)), f2 < 0.5),
    Or(Not(And(x1 >= 0.5, x2 >= 0.5)), f2 < 0.5),
    Or(Not(And(x1 < 0.5, x2 >= 0.5)), f2 >= 0.5),
    Or(Not(And(x1 >= 0.5, x2 < 0.5)), f2 >= 0.5)
)
)


print(s.check())

print(s.sexpr()) # .smtlib형태로 치환하여 출력해줌

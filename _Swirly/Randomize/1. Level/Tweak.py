# Copyright (c) 2010, Tom Swirly

# Released as open source under the "IDC" license - "I Don't Care" what you do
# with it as long as I and everyone else can continue to unconditionally use it
# and make derivative works from it.

# import math
# import random

import Swirly

selected = GetAllSelCh(False)

if not selected:
  Message("Select some channels first!")

print map(GetChVal, range(16))

for ch in selected:
  SetChVal(ch, int(Swirly.rand.perturbDMX(GetChVal(ch), 0.25)))


def deco(f):
  def g(x):
    return f(x + 1)
  return g

@deco
def h(x):
  return x + 10

print h(23)

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

for ch in selected:
  SetChVal(ch, Swirly.rand.dmx())

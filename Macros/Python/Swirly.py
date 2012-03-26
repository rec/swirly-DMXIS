# Copyright (c) 2010, Tom Swirly

# Released as open source under the "IDC" license - "I Don't Care" what you do
# with it as long as I and everyone else can continue to unconditionally use it
# and make derivative works from it.


def limitDMX(x):
  if x < 0:
    return 0
  if x > 255:
    return 255
  return x


# Fast, fake random numbers to compensate for not having the Python math
# library.  See http://en.wikipedia.org/wiki/Linear_congruential_generator

class Rand:
  def __init__(self, seed, a=1664525, c=1013904223, m=(2 ** 32)):
    self.seed = seed;
    self.a = a
    self.c = c
    self.m = m
    self.randomize()

  def randomize(self):
    self.seed = ((self.a * self.seed) + self.c) % self.m

  def randInt(self, n):
    self.randomize()
    return (n * self.seed) / self.m

  def dmx(self):
    return self.randInt(256)

  def perturb(self, value, amount):
    return value + self.randInt(2 * amount + 1) - amount

  def perturbDMX(self, value, ratio):
    return limitDMX(int(self.perturb(value, 128 * ratio)))


rand = Rand(42)

def process(fn, data, channels, getter, setter):
  for c in channels:
    setter(c, fn(getter(c), data))


def processor(data):
  def decorator(fn):
    def f(channels, getter, setter):
      for c in channels:
        setter(c, fn(getter(c), data))
    return f

  return decorator

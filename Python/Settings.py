#!/usr/local/bin/python

NAMES = {
  "invert": "i",

  "level": "fg",
  "band": "ff",
  "attack": "fa",
  "release": "fr",
  "dir": "fd",

  "type": "t",
  "amount": "a",
  "chase": "p",
  "speed": "s",
  "shape": "sh",

  "value": "v",
  "controller": "cc",
  "channel": "ch",

  # I'm not really sure what these symbols mean.
  "en": "en",
  "nrpn": "nrpn",
  "tm": "tm",
  }

def Translate(*args, **kwds):
  if kwds:
    if args:
      raise Exception("Can't have both list and keyword arguments")
    else:
      return dict((NAMES.get(k, k), v) for k, v in kwds)
  return [NAMES.get(k, k) for k in args]


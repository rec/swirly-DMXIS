#!/usr/local/bin/python

# We'd like long names for the very short names that ENTTEC uses.

KEY_NAMES = {
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
  # "en": "en",
  # "nrpn": "nrpn",
  # "tm": "tm",
}

def Translate(*args, **kwds):
  """Translate a list or dictionary of items from the full names to ENTTEC's
  internal names."""
  if kwds:
    if args:
      raise Exception("Can't have both list and keyword arguments")
    else:
      return dict((KEY_NAMES.get(k, k), TranslateOsc(k, v))
                  for k, v in kwds.iteritems())

  return [KEY_NAMES.get(k, k) for k in args]

KEY_TYPES = {
  'DmxUniverse': frozenset(Translate(*[
    'amount', 'attack', 'dir', 'band', 'level', 'release', 'invert', 'chase',
    'speed', 'shape', 'type', 'en', 'tm'])),

  'Params': frozenset(Translate(*['value', 'controller', 'channel', 'nprn']))
}

# We want to name oscillator types as strings, not numbers.

OSCILLATOR_TYPES = ['off', 'sine', 'square', 'triangle', 'saw up', 'saw dn']
OSCILLATOR_MAP = dict((x, i) for i, x in enumerate(OSCILLATOR_TYPES))

def TranslateOsc(k, v):
  return v if k != OSCILLATOR_TYPE_KEY else OSCILLATOR_MAP.get(v, v)

OSCILLATOR_TYPE_KEY = Translate('type')[0]

def TranslateAll(faders):
  return dict((k, Translate(**v)) for k, v in faders.iteritems())

def SelectAttributes(tagname, attr):
  print tagname
  return dict((k, v) for k, v in attr.iteritems() if k in KEY_TYPES[tagname])

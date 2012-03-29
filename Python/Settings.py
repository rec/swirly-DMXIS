#!/usr/local/bin/python

# SETTINGS maps human-readable names to the short names that ENTTEC uses.
SETTINGS = {
  "invert": "i",
  "enable": "en",

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
  # "nrpn": "nrpn",
  # "tm": "tm",
}

def ToMap(*args):
  """Converts a list of values into a map from the value to its index.
  Example:  ToMap('a', 'b', 'c') returns {'a': '0', 'b': '1', 'c': '2'}
  """
  return dict((v, str(i)) for i, v in enumerate(args))

# VALUES maps meaningful text names to the ENTTEC numeric values.
VALUES = {
  SETTINGS['dir']: ToMap('up', 'down'),
  SETTINGS['band']: ToMap('sub', 'lo', 'mid', 'hi'),
  SETTINGS['invert']: ToMap('off', 'on'),
  SETTINGS['speed']: ToMap('1/16', '1/8', '3/16', '1/4', '3/8', '1/2', '3/4',
                           '1', '2', '3', '4', '6', '8', '12', '16', '24', '32',
                           '48', '64', '96', '128'),
  SETTINGS['type']: ToMap('off', 'sine', 'square', 'triangle', 'saw up',
                          'saw dn'),
}

def TranslateKeyValue(key, value):
  """Translate a key, value pair from human-readable form to ENTTEC's data
  format."""
  key = SETTINGS.get(key, key)
  value = VALUES.get(key, {}).get(value, value)
  return key, value

def TranslateDict(d):
  """Translate dictionary of items from the full names to ENTTEC's internal data
  format."""

  return dict(TranslateKeyValue(k, v) for  k, v in d.iteritems())

def TranslateList(*items):
    return [SETTINGS.get(k, k) for k in items]

ATTRIBUTES = {
  'c': TranslateList(
    'amount', 'attack', 'dir', 'band', 'level', 'release', 'invert', 'chase',
    'speed', 'shape', 'type', 'enable', 'tm'),

  'Param': TranslateList('value', 'controller', 'channel', 'nprn')
}

def SelectAttributes(tagname, attr):
  return dict((k, v) for k, v in attr.iteritems() if k in ATTRIBUTES[tagname])

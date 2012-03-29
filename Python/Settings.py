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
  "nrpn": "nrpn",
  "tm": "tm",
}

SETTINGS_INVERSE = dict((v, k) for k, v in SETTINGS.iteritems())

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
  SETTINGS['speed']: ToMap('1/16 note', '1/8 note', '3/16 note', '1/4 note',
                           '3/8 note', '1/2 note', '3/4 note', '1 bar',
                           '2 bars', '3 bars', '4 bars', '6 bars', '8 bars',
                           '12 bars', '16 bars', '24 bars', '32 bars',
                           '48 bars', '64 bars', '96 bars', '128 bars'),
  SETTINGS['type']: ToMap('off', 'sine', 'square', 'triangle', 'saw up',
                          'saw dn'),
}

def TranslateKeyValue(key, value):
  """Translate a key, value pair from human-readable form to ENTTEC's data
  format."""
  key = SETTINGS.get(key, key)
  if key not in SETTINGS_INVERSE:
    raise Exception("Didn't understand key %s" % key)

  valueMap = VALUES.get(key, {})
  if valueMap:
    value = valueMap.get(value, value)
    if not value.isdigit() or int(value) < 0 or int(value) >= len(valueMap):
      raise Exception("Didn't understand value %s for key %s" % (value, key))

  else:
    parts = (value[1:] if value.startswith('-') else value).split('.')
    error = None
    if len(parts) is 0:
      error = 'Empty'
    elif len(parts) > 2:
      error = 'Too many . in'
    elif not parts[0].isdigit():
      error = 'Non-digit in'
    elif len(parts) is 2 and not parts[1].isdigit():
      error = 'Non-digit in'

    if error:
      raise 'Exception: %s number %s for key %s' % (value, key)

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

  'Param': TranslateList('value', 'controller', 'channel', 'nrpn')
}

def SelectAttributes(tagname, attr):
  return dict((k, v) for k, v in attr.iteritems() if k in ATTRIBUTES[tagname])

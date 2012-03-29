#!/usr/local/bin/python

"""
Write a bank of DMXIS presets given a much-simpler JSON description file.

Usage:  WriteBank.py bank-desc.json.

See the file test.json in this directory for another example.

"""

# System imports.
import sys

# Try to import the YAML parser, else fall back to JSON.
try:
  import yaml
  Load = yaml.load

except ImportError:
  import json

  Load = json.load

# My imports.
import Preset
import Xml

def PresetAttributes(p):
  return dict(crossfade=p.get('crossfade', '0.000000'), name=p['name'])

def WriteBank(filename):
  bank = Load(open(filename))
  document = Xml.CreateDocument('Order')
  root = document.documentElement

  for preset in bank['presets']:
    Preset.Preset(preset).Write()
    Xml.CreateElement(document, root, 'Preset', PresetAttributes(preset))

  output = Xml.WriteTo(document, 'bank', '.xml')
  output.write('<Tempo val="%s" />\n' % bank.get('tempo', '120.000000'))

if __name__ == '__main__':
  if len(sys.argv) is not 2:
    print 'Usage: %s json-filename' % sys.argv[0]
    sys.exit(-1)

  WriteBank(sys.argv[1])


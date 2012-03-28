#!/usr/local/bin/python

"""
Write a bank of DMXIS presets given a much-simpler JSON description file.

Usage:  WriteBank.py bank-desc.json.

See the file test.json in this directory for more examples.

"""

# System imports.
import json
import sys

# My imports.
import Preset
import Xml

def PresetAttributes(p):
  return dict(crossfade=p.get('crossfade', '0.000000'), name=p['name'])

def WriteBank(filename):
  bank = json.load(open(filename))
  document = Xml.CreateDocument('Order')
  root = document.documentElement

  for preset in bank['presets']:
    Preset.Preset(preset).Write()
    Xml.CreateElement(document, root, 'Preset', PresetAttributes(preset))

  output = Xml.WriteTo(document, bank['name'], '.xml')
  output.write('<Tempo val="%s" />\n' % bank.get('tempo', '120.000000'))

if __name__ == '__main__':
  if len(sys.argv) is not 2:
    print 'Usage: %s json-filename' % sys.argv[0]
    sys.exit(-1)

  WriteBank(sys.argv[1])


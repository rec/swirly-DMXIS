#!/usr/local/bin/python

"""
Write a bank of DMXIS presets given a much-simpler JSON description file.

Usage:  WriteBank.py bank-desc.json.

See the file test.json in this directory for more examples.

"""

# System imports.
import json
import os.path
import sys

# My imports.
import Adder
import Defaults
import Settings
import Xml

def OpenFile(name, suffix='.xml', mode='w'):
  if not name.endswith(suffix):
    name += suffix
  return open(name, mode)


def WritePreset(bank):
  name = bank['name']
  d = dict(defaults.PRESET_DEFAULTS, name=name)
  document = Xml.CreateDocument('DbAudiowarePreset', d)
  root = document.documentElement

  Params.Add(root, bank)
  AddUniverse(root, bank)
  WriteXml(root, OpenFile(name, '.prt'))


def WriteBank(bank):
  document = Xml.CreateDocument('Order')
  root = document.documentElement
  with OpenFile(bank['name']) as output:
    WriteXml(root, output)
    output.write('<Tempo val="%s" />\n' % bank.get('tempo', '120.000000'))


def WriteBankAndPresets(filename):
  bank = json.load(open(filename))
  for preset in bank['presets']:
    WritePreset(preset)

  WriteBank(bank)


if __name__ == '__main__':
  if len(sys.argv) is not 2:
    print 'Usage: %s json-filename' % sys.argv[0]
    sys.exit(-1)

  WriteBankAndPresets(sys.argv[1])


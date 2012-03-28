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
import Defaults
import xml


C_SETTINGS = Settings.Translate(*['amount', 'attack', 'dir', 'band', 'level',
                                  'release', 'invert', 'chase', 'speed', 'shape',
                                  'type', 'en', 'tm'])

PRESET_SETTINGS = TranslateSettings(*['value', 'controller', 'channel', 'nprn'])

PARAM_FIRST = [
  'X Value', 'Bank', 'Preset', 'PresetUp', 'PresetDown', 'ShowPresetPage',
  'BankUp', 'BankDown', 'NewPreset', 'DeletePreset', 'EditPreset', 'NewBank',
  'DeleteBank', 'EditBank', 'SortMode', 'Autoplay Bank', 'OverwrtPst']

PARAM_SECOND = [
  'DmxNextPage', 'DmxPrevPage', 'Master Speed', 'MasterTempo', 'Macros',
  'Grand Master', 'Crossfade', 'Type', 'Amount', 'Offset', 'Speed', 'Shape',
  'Band', 'Level', 'Attack', 'Release', 'Dir', 'Invert']

OSCILLATOR_TYPES = ['off', 'sine', 'square', 'triangle', 'saw up', 'saw dn']

def OpenFile(name, suffix, mode='w'):
  if not name.endswith(suffix):
    name += suffix
  return open(name, mode)

def AddElements(document, names, data, tag, parent, nameField):
  sub = data.get(tag, {})
  omit = set(sub.get("OMIT", []))
  for name in names:
    if name not in omit:
      d = sub.get(name, {})
      d = dict((str(k), v) for k, v in d.iteritems())
      attributes = defaults.GetDefault(tag, {nameField: name}, d)
      xml.CreateElement(document, parent, tag, attributes)

def WritePreset(bank):
  name = bank['name']
  d = dict(defaults.PRESET_DEFAULTS, name=name)
  document = xml.CreateDocument('DbAudiowarePreset', d)
  root = document.documentElement
  params = xml.CreateElement(document, root, 'Params')
  dmx = xml.CreateElement(document, root, 'DmxUniverse')



  AddElements(document, defaults.PARAM_NAMES, data, 'Param', params, 'nm')
  AddElements(document, defaults.DMX_NAMES, data, 'c', dmx, 'n')
  WriteXml(root, OpenFile(name, '.prt'))


def WriteBank(bank):
  document = xml.CreateDocument('Order')
  root = document.documentElement
  with OpenFile(bank['name'], '.xml') as output:
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


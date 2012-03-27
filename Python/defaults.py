#!/usr/local/bin/python

import OrderedDict

PRESET_PARTS = {
  'DbAudiowarePreset': OrderedDict.OrderedDict([
    ['product', 'DMXIS'],
    ['major', '1'],
    ['minor', '2'],
    ['patch', '0'],
    ['algoname', 'DMXIS'],
  ]),

  'Param': OrderedDict.OrderedDict([
    ['v', '0.000000'],
    ['cc', '-1'],
    ['nrpn', '-1'],
    ['ch', '0'],
  ]),

  'c': OrderedDict.OrderedDict([
    ['t', '0'],
    ['a', '0.500000'],
    ['p', '0.000000'],
    ['s', '7'],
    ['tm', '10.000000'],
    ['sh', '0.500000'],
    ['i', '0'],
    ['en', '1'],
    ['fa', '1.000000'],
    ['fr', '49.987503'],
    ['fg', '0'],
    ])
  }

DMX_NAMES = [str(i) for i in xrange(1, 513)]

PARAM_FIRST = [
  'X Value', 'Bank', 'Preset', 'PresetUp', 'PresetDown', 'ShowPresetPage',
  'BankUp', 'BankDown', 'NewPreset', 'DeletePreset', 'EditPreset', 'NewBank',
  'DeleteBank', 'EditBank', 'SortMode', 'Autoplay Bank', 'OverwrtPst']

PARAM_SECOND = [
  'DmxNextPage', 'DmxPrevPage', 'Master Speed', 'MasterTempo', 'Macros',
  'Grand Master', 'Crossfade', 'Type', 'Amount', 'Offset', 'Speed', 'Shape',
  'Band', 'Level', 'Attack', 'Release', 'Dir', 'Invert']

PARAM_NAMES = PARAM_FIRST + DMX_NAMES + PARAM_SECOND

CHANNEL_SETTING_MAP = dict(
  invert='i',
  level='fg',
  band='ff',
  attack='fa',
  release='fr',
  dir='fd',
  type='t',
  amount='a',
  chase='p',
  speed='s',
  shape='sh')

def GetDefault(name, primary, secondary):
  d = OrderedDict.OrderedDict(primary)
  d.update(PRESET_PARTS[name])
  d.update(secondary)
  return d


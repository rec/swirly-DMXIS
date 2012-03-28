#!/usr/local/bin/python

import Default
import Settings
import Xml

class Preset(object):
  BEFORE = [
    'X Value', 'Bank', 'Preset', 'PresetUp', 'PresetDown', 'ShowPresetPage',
    'BankUp', 'BankDown', 'NewPreset', 'DeletePreset', 'EditPreset', 'NewBank',
    'DeleteBank', 'EditBank', 'SortMode', 'Autoplay Bank', 'OverwrtPst']

  FADERS = [str(i + 1) for i in xrange(512)]

  AFTER = [
    'DmxNextPage', 'DmxPrevPage', 'Master Speed', 'MasterTempo', 'Macros',
    'Grand Master', 'Crossfade', 'Type', 'Amount', 'Offset', 'Speed', 'Shape',
    'Band', 'Level', 'Attack', 'Release', 'Dir', 'Invert']

  TOP_TAGS = ['DmxUniverse', 'Params']
  TAGS = ['c', 'Param']
  ATTR_NAMES = ['n', 'nm']

  def __init__(self, preset):
    self.omit = preset.get('omit', [])
    self.faderSettings = Settings.TranslateAll(preset.get('faders', {}))
    self.name = preset['name']

  def Write(self):
    d = dict(Default.PRESET, name=self.name)
    self.document = Xml.CreateDocument('DbAudiowarePreset', d)
    self.root = self.document.documentElement
    self._Add(True)
    self._Add(False)

    Xml.WriteTo(self.document, self.name, '.prt')

  def _Add(self, isParam):
    self.element = self._Create(self.root, Preset.TOP_TAGS[isParam])
    self.attrName = Preset.ATTR_NAMES[isParam]
    self.tag = Preset.TAGS[isParam]

    if isParam:
      self._AddSegment(Preset.BEFORE)
      self._AddSegment(Preset.FADERS)
      self._AddSegment(Preset.AFTER)
    else:
      self._AddSegment(Preset.FADERS, lambda x: str(int(x) - 1))

  def _AddSegment(self, faders, nameMaker=lambda x: x):
    for fader in faders:
      if fader not in self.omit:
        fader = nameMaker(fader)
        attr = dict(Default.FADER)
        attr.update(self.faderSettings.get(fader, {}))
        attr = Settings.SelectAttributes(self.tag, attr)
        attr[self.attrName] = fader
        self._Create(self.element, self.tag, attr)

  def _Create(self, parent, tagname, attr={}):
    return Xml.CreateElement(self.document, parent, tagname, attr)

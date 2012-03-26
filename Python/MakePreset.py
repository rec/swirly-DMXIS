import json
import xml.etree.ElementTree as ElementTree

import defaults

USE_ETREE = True

if USE_ETREE:
  def CreateRootElement(tag, **attributes):
    return ElementTree.Element(tag, attributes)

  def CreateElement(parent, tag, **attributes):
    return ElementTree.SubElement(parent, tag, attributes)

  def Print(root, output):
    ElementTree.ElementTree(root).write(output)


def Add(names, data, tag, parent, nameField):
  sub = data[tag]
  for name in names:
    d = dict(sub.get(name, {}))
    d[nameField] = name
    d = dict((str(k), v) for k, v in d.iteritems())
    CreateElement(parent, tag, **defaults.Get(tag, **d))


def MakePreset(input, output):
  data = json.load(input)
  d = defaults.Get('DbAudiowarePreset', name=data['name'])
  root = CreateRootElement('DbAudiowarePreset', **d)
  params = CreateElement(root, 'Params')
  dmx = CreateElement(root, 'DmxUniverse')

  Add(defaults.PARAM_NAMES, data, 'Param', params, 'nm')
  Add(defaults.DMX_NAMES, data, 'c', dmx, 'n')

  Print(root, output)


with open('sample.json') as input:
  with open('sample.xml', 'w') as output:
    MakePreset(input, output)

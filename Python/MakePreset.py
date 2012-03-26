import json
import xml.etree.ElementTree as ElementTree

import defaults

def Add(names, data, tag, parent, nameField):
  sub = data[tag]
  for name in names:
    d = dict(sub.get(name, {}))
    d[nameField] = name
    d = dict((str(k), v) for k, v in d.iteritems())
    df = defaults.Get(tag, **d)
    ElementTree.SubElement(parent, tag, df)


def Translate(input, output):
  data = json.load(input)
  d = defaults.Get('DbAudiowarePreset', name=data['name'])
  root = ElementTree.Element('DbAudiowarePreset', d)
  params = ElementTree.SubElement(root, 'Params')
  dmx = ElementTree.SubElement(root, 'DmxUniverse')

  Add(defaults.PARAM_NAMES, data, 'Param', params, 'nm')
  Add(defaults.DMX_NAMES, data, 'c', dmx, 'n')

  ElementTree.ElementTree(root).write(output)


with open('sample.json') as input:
  with open('sample.xml', 'w') as output:
    Translate(input, output)

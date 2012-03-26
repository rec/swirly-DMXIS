import json
import xml.dom.minidom

import defaults

def SetNodeValue(node, **kwds):
  for k, v in kwds.iteritems():
    node.setAttribute(k, v)

def CreateDocument(tag, **attributes):
  impl = xml.dom.minidom.getDOMImplementation()
  document = impl.createDocument(None, tag, None)
  SetNodeValue(document.documentElement, **attributes)
  return document

def CreateElement(document, parent, tag, **attributes):
  element = document.createElement(tag)
  SetNodeValue(element, **attributes)
  parent.appendChild(element)
  return element

def Print(document, output):
  output.write(document.toprettyxml(indent='  '))

def Add(document, names, data, tag, parent, nameField):
  sub = data[tag]
  for name in names:
    d = dict(sub.get(name, {}))
    d[nameField] = name
    d = dict((str(k), v) for k, v in d.iteritems())
    CreateElement(document, parent, tag, **defaults.Get(tag, **d))

def MakePreset(data, output):
  d = defaults.Get('DbAudiowarePreset', name=data['name'])
  document = CreateDocument('DbAudiowarePreset', **d)
  root = document.documentElement
  params = CreateElement(document, root, 'Params')
  dmx = CreateElement(document, root, 'DmxUniverse')

  Add(document, defaults.PARAM_NAMES, data, 'Param', params, 'nm')
  Add(document, defaults.DMX_NAMES, data, 'c', dmx, 'n')

  Print(root, output)

if __name__ == '__main__':
  with open('sample.json') as input:
    data = json.load(input)
    with open('sample.xml', 'w') as output:
      MakePreset(data, output)

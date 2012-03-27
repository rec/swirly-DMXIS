#!/usr/local/bin/python

"""
Write a bank of DMXIS presets given a much-simpler JSON description file.

Usage:  WriteBank.py bank-desc.json.

See the file test.json in this directory for more examples.

"""

import json
import os.path
import sys
import xml.dom.minidom

import defaults
import OrderedDict

def SetNodeValue(node, kwds):
  for k, v in kwds.iteritems():
    # STUPID xml.dom.minidom sorts the attributes when it gets them.  :-(
    node.setAttribute(k, v)

def CreateDocument(tag, attributes):
  impl = xml.dom.minidom.getDOMImplementation()
  document = impl.createDocument(None, tag, None)
  SetNodeValue(document.documentElement, attributes)
  return document

def CreateElement(document, parent, tag, attributes={}):
  element = document.createElement(tag)
  SetNodeValue(element, attributes)
  parent.appendChild(element)
  return element

def Print(document, output):
  output.write(document.toprettyxml(indent='  '))

def Add(document, names, data, tag, parent, nameField):
  sub = data.get(tag, {})
  omit = set(sub.get("OMIT", []))
  for name in names:
    if name not in omit:
      d = sub.get(name, {})
      d = OrderedDict.OrderedDict((str(k), v) for k, v in d.iteritems())
      attributes = defaults.GetDefault(tag, {nameField: name}, d)
      CreateElement(document, parent, tag, attributes)

def MakePreset(name, data, output):
  d = defaults.GetDefault('DbAudiowarePreset', dict(name=name), {})
  document = CreateDocument('DbAudiowarePreset', d)
  root = document.documentElement
  params = CreateElement(document, root, 'Params')
  dmx = CreateElement(document, root, 'DmxUniverse')

  Add(document, defaults.PARAM_NAMES, data, 'Param', params, 'nm')
  Add(document, defaults.DMX_NAMES, data, 'c', dmx, 'n')

  Print(root, output)

def WriteBank(bank):
  for name, subdata in bank.iteritems():
    with open(name + '.xml', 'w') as output:
      MakePreset(name, subdata, output)

if __name__ == '__main__':
  if len(sys.argv) is 2:
    with open(sys.argv[1]) as input:
      WriteBank(json.load(input))
  else:
    print 'Usage: %s json-filename' % sys.argv[0]
    sys.exit(-1)

#!/usr/local/bin/python

import xml.dom.minidom

def SetNodeValue(node, kwds):
  for k, v in kwds.iteritems():
    # STUPID xml.dom.minidom sorts the attributes when it gets them.  :-(
    node.setAttribute(k, v)

def CreateDocument(tag, attributes={}):
  impl = xml.dom.minidom.getDOMImplementation()
  document = impl.createDocument(None, tag, None)
  SetNodeValue(document.documentElement, attributes)
  return document

def CreateElement(document, parent, tag, attributes={}):
  element = document.createElement(tag)
  SetNodeValue(element, attributes)
  parent.appendChild(element)
  return element

def Write(document, output):
  output.write(document.toprettyxml(indent='  '))

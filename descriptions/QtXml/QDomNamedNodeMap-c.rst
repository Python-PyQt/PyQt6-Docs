.. sip:class-description::
    :status: todo
    :brief: Contains a collection of nodes that can be accessed by name
    :digest: 77e911090b0b86674401ee930a7b2811

The :sip:ref:`~PyQt6.QtXml.QDomNamedNodeMap` class contains a collection of nodes that can be accessed by name.

Note that :sip:ref:`~PyQt6.QtXml.QDomNamedNodeMap` does not inherit from :sip:ref:`~PyQt6.QtXml.QDomNodeList`. QDomNamedNodeMaps do not provide any specific node ordering. Although nodes in a :sip:ref:`~PyQt6.QtXml.QDomNamedNodeMap` may be accessed by an ordinal index, this is simply to allow a convenient enumeration of the contents of a :sip:ref:`~PyQt6.QtXml.QDomNamedNodeMap`, and does not imply that the DOM specifies an ordering of the nodes.

The :sip:ref:`~PyQt6.QtXml.QDomNamedNodeMap` is used in three places:

#. :sip:ref:`~PyQt6.QtXml.QDomDocumentType.entities` returns a map of all entities described in the DTD.

#. :sip:ref:`~PyQt6.QtXml.QDomDocumentType.notations` returns a map of all notations described in the DTD.

#. :sip:ref:`~PyQt6.QtXml.QDomNode.attributes` returns a map of all attributes of an element.

Items in the map are identified by the name which QDomNode::name() returns. Nodes are retrieved using :sip:ref:`~PyQt6.QtXml.QDomNamedNodeMap.namedItem`, :sip:ref:`~PyQt6.QtXml.QDomNamedNodeMap.namedItemNS` or :sip:ref:`~PyQt6.QtXml.QDomNamedNodeMap.item`. New nodes are inserted with :sip:ref:`~PyQt6.QtXml.QDomNamedNodeMap.setNamedItem` or :sip:ref:`~PyQt6.QtXml.QDomNamedNodeMap.setNamedItemNS` and removed with :sip:ref:`~PyQt6.QtXml.QDomNamedNodeMap.removeNamedItem` or :sip:ref:`~PyQt6.QtXml.QDomNamedNodeMap.removeNamedItemNS`. Use :sip:ref:`~PyQt6.QtXml.QDomNamedNodeMap.contains` to see if an item with the given name is in the named node map. The number of items is returned by :sip:ref:`~PyQt6.QtXml.QDomNamedNodeMap.length`.

Terminology: in this class we use "item" and "node" interchangeably.

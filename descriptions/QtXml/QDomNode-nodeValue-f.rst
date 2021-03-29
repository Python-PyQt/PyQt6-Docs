.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 4e8f4214d9d64051fa5b97eeb37316d5

Returns the value of the node.

The meaning of the value depends on the subclass:

+---------------------------------------------------+----------------------------------------+
| Name                                              | Meaning                                |
+===================================================+========================================+
| :sip:ref:`~PyQt6.QtXml.QDomAttr`                  | The attribute value                    |
+---------------------------------------------------+----------------------------------------+
| :sip:ref:`~PyQt6.QtXml.QDomCDATASection`          | The content of the CDATA section       |
+---------------------------------------------------+----------------------------------------+
| :sip:ref:`~PyQt6.QtXml.QDomComment`               | The comment                            |
+---------------------------------------------------+----------------------------------------+
| :sip:ref:`~PyQt6.QtXml.QDomProcessingInstruction` | The data of the processing instruction |
+---------------------------------------------------+----------------------------------------+
| :sip:ref:`~PyQt6.QtXml.QDomText`                  | The text                               |
+---------------------------------------------------+----------------------------------------+

All the other subclasses do not have a node value and will return an empty string.

.. seealso:: :sip:ref:`~PyQt6.QtXml.QDomNode.setNodeValue`, :sip:ref:`~PyQt6.QtXml.QDomNode.nodeName`.

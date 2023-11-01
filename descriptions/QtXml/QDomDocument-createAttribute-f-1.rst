.. sip:method-description::
    :status: todo
    :pysig: ebd432c04eed54b748f914db709409d5
    :realsig: (const QString&)
    :digest: a36cfa3bf7d79bed00ff867b160ee31d

Creates a new attribute called *name* that can be inserted into an element, e.g. using :sip:ref:`~PyQt6.QtXml.QDomElement.setAttributeNode`.

If *name* is not a valid XML name, the behavior of this function is governed by :sip:ref:`~PyQt6.QtXml.QDomImplementation.InvalidDataPolicy`.

.. seealso:: :sip:ref:`~PyQt6.QtXml.QDomDocument.createAttributeNS`.

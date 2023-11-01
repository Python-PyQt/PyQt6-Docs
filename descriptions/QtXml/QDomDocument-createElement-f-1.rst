.. sip:method-description::
    :status: todo
    :pysig: 3e2636b2cffe86be560dd59cf9f1bf41
    :realsig: (const QString&)
    :digest: 3f933f6b77f302aafe683e8e18f0a8fb

Creates a new element called *tagName* that can be inserted into the DOM tree, e.g. using :sip:ref:`~PyQt6.QtXml.QDomNode.appendChild`.

If *tagName* is not a valid XML name, the behavior of this function is governed by :sip:ref:`~PyQt6.QtXml.QDomImplementation.InvalidDataPolicy`.

.. seealso:: :sip:ref:`~PyQt6.QtXml.QDomDocument.createElementNS`, :sip:ref:`~PyQt6.QtXml.QDomNode.appendChild`, :sip:ref:`~PyQt6.QtXml.QDomNode.insertBefore`, :sip:ref:`~PyQt6.QtXml.QDomNode.insertAfter`.

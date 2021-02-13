.. sip:method-description::
    :status: todo
    :pysig: 72fd2c896439ef4dcacba45a738c8b55
    :realsig: (const QString&)
    :digest: 67298b96bb3492ac78071b99390d96fc

Creates a text node for the string *value* that can be inserted into the document tree, e.g. using :sip:ref:`~PyQt6.QtXml.QDomNode.appendChild`.

If *value* contains characters which cannot be stored as character data of an XML document (even in the form of character references), the behavior of this function is governed by :sip:ref:`~PyQt6.QtXml.QDomImplementation.InvalidDataPolicy`.

.. seealso:: :sip:ref:`~PyQt6.QtXml.QDomNode.appendChild`, :sip:ref:`~PyQt6.QtXml.QDomNode.insertBefore`, :sip:ref:`~PyQt6.QtXml.QDomNode.insertAfter`.

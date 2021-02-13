.. sip:method-description::
    :status: todo
    :pysig: cbc56f27be1c0842c8a3688c5ab89930
    :realsig: (const QString&)
    :digest: 6a95e61859e3868a9c0f45c290230c97

Creates a new comment for the string *value* that can be inserted into the document, e.g. using :sip:ref:`~PyQt6.QtXml.QDomNode.appendChild`.

If *value* contains characters which cannot be stored in an XML comment, the behavior of this function is governed by :sip:ref:`~PyQt6.QtXml.QDomImplementation.InvalidDataPolicy`.

.. seealso:: :sip:ref:`~PyQt6.QtXml.QDomNode.appendChild`, :sip:ref:`~PyQt6.QtXml.QDomNode.insertBefore`, :sip:ref:`~PyQt6.QtXml.QDomNode.insertAfter`.

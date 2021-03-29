.. sip:method-description::
    :status: todo
    :pysig: 5a020d70d93caeb07b93577c5955512e
    :realsig: (const QString&)
    :digest: 8588cee237cf24385805a9db1cf873d8

Creates a new CDATA section for the string *value* that can be inserted into the document, e.g. using :sip:ref:`~PyQt6.QtXml.QDomNode.appendChild`.

If *value* contains characters which cannot be stored in a CDATA section, the behavior of this function is governed by :sip:ref:`~PyQt6.QtXml.QDomImplementation.InvalidDataPolicy`.

.. seealso:: :sip:ref:`~PyQt6.QtXml.QDomNode.appendChild`, :sip:ref:`~PyQt6.QtXml.QDomNode.insertBefore`, :sip:ref:`~PyQt6.QtXml.QDomNode.insertAfter`.

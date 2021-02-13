.. sip:method-description::
    :status: todo
    :pysig: 84af79e299d9678523f1fd5d1e5357a9
    :realsig: (const QString&,const QString&)
    :digest: 34179fee06994f8a2f01fb2db7450560

Creates a new processing instruction that can be inserted into the document, e.g. using :sip:ref:`~PyQt6.QtXml.QDomNode.appendChild`. This function sets the target for the processing instruction to *target* and the data to *data*.

If *target* is not a valid XML name, or data if contains characters which cannot appear in a processing instruction, the behavior of this function is governed by :sip:ref:`~PyQt6.QtXml.QDomImplementation.InvalidDataPolicy`.

.. seealso:: :sip:ref:`~PyQt6.QtXml.QDomNode.appendChild`, :sip:ref:`~PyQt6.QtXml.QDomNode.insertBefore`, :sip:ref:`~PyQt6.QtXml.QDomNode.insertAfter`.

.. sip:method-description::
    :status: todo
    :pysig: e612959cce3384377096da513430948a
    :realsig: (const QString&)
    :digest: 9f22b472142135a2f30c7f466e6ef3f5

Creates a new entity reference called *name* that can be inserted into the document, e.g. using :sip:ref:`~PyQt6.QtXml.QDomNode.appendChild`.

If *name* is not a valid XML name, the behavior of this function is governed by :sip:ref:`~PyQt6.QtXml.QDomImplementation.InvalidDataPolicy`.

.. seealso:: :sip:ref:`~PyQt6.QtXml.QDomNode.appendChild`, :sip:ref:`~PyQt6.QtXml.QDomNode.insertBefore`, :sip:ref:`~PyQt6.QtXml.QDomNode.insertAfter`.

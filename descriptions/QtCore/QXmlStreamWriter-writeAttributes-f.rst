.. sip:method-description::
    :status: todo
    :pysig: ea0687d043886e5ccd79e09f851ce5be
    :realsig: (const QXmlStreamAttributes&)
    :digest: f0f9bc27ecef32def8db99c91546acd9

Writes the attribute vector *attributes*. If a namespace referenced in an attribute not been declared yet, :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter` will generate a namespace declaration for it.

This function can only be called after :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.writeStartElement` before any content is written, or after :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.writeEmptyElement`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.writeAttribute`, :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.writeNamespace`.

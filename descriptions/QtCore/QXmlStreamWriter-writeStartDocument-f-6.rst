.. sip:method-description::
    :status: todo
    :pysig: 469c3d5de45760d2e753a158b05ea5cb
    :realsig: (QAnyStringView, bool)
    :digest: 6b5a78066264a2d70b19d22fe6256852

Writes a document start with the XML version number *version* and a standalone attribute *standalone*.

**Note:** This function does not validate the version string and allows setting it manually. However, :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter` only supports XML 1.0. Setting a version string other than "1.0" does not change the writer's behavior or escaping rules. It is the caller's responsibility to ensure consistency between the declared version and the actual content.

**Note:** In Qt versions prior to 6.5, this function took QString, not QAnyStringView.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter.writeEndDocument`.

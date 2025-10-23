.. sip:method-description::
    :status: todo
    :pysig: fefbb0d692768e1442b6d892fc80cf0c
    :realsig: (QIODevice*,const char*,int) const
    :digest: 93d8b67df46d564212de22eae613f422

This function writes a :sip:ref:`~PyQt6.QtGui.QPixmap` to the given *device* using the specified image file *format* and *quality* factor. This can be used, for example, to save a pixmap directly into a :sip:ref:`~PyQt6.QtCore.QByteArray`:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-image-image.py
    :lines: 70-74

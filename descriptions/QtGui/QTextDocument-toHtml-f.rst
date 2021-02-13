.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 82ce945c8c4df36f821ea2d8fb103801

Returns a string containing an HTML representation of the document.

The content of the document specifies its encoding to be UTF-8. If you later on convert the returned html string into a byte array for transmission over a network or when saving to disk you should use QString::toUtf8() to convert the string to a :sip:ref:`~PyQt6.QtCore.QByteArray`.

.. seealso:: `Supported HTML Subset <https://doc.qt.io/qt-6/richtext-html-subset.html>`_.

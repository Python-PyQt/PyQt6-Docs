.. sip:method-description::
    :status: todo
    :pysig: 17c56a01dd1565f39cc04f7d142fd4f4
    :realsig: (QStringConverter::Encoding)
    :digest: b554054f59c8e0d3934c18a9a501fc15

Sets the encoding for this stream to *encoding*. The encoding is used for decoding any data that is read from the assigned device, and for encoding any data that is written. By default, :sip:ref:`~PyQt6.QtCore.QStringConverter.Encoding.Utf8` is used, and automatic unicode detection is enabled.

If :sip:ref:`~PyQt6.QtCore.QTextStream` operates on a string, this function does nothing.

**Warning:** If you call this function while the text stream is reading from an open sequential socket, the internal buffer may still contain text decoded using the old encoding.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTextStream.encoding`, :sip:ref:`~PyQt6.QtCore.QTextStream.setAutoDetectUnicode`, :sip:ref:`~PyQt6.QtCore.QTextStream.setLocale`.

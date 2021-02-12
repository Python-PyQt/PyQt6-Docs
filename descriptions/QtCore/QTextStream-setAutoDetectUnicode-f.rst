.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 144abe8daed8cd44fa09e764d04d4b7b

If *enabled* is true, :sip:ref:`~PyQt6.QtCore.QTextStream` will attempt to detect Unicode encoding by peeking into the stream data to see if it can find the UTF-8, UTF-16, or UTF-32 Byte Order Mark (BOM). If this mark is found, :sip:ref:`~PyQt6.QtCore.QTextStream` will replace the current encoding with the UTF encoding.

This function can be used together with :sip:ref:`~PyQt6.QtCore.QTextStream.setEncoding`. It is common to set the encoding to UTF-8, and then enable UTF-16 detection.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTextStream.autoDetectUnicode`, :sip:ref:`~PyQt6.QtCore.QTextStream.setEncoding`.

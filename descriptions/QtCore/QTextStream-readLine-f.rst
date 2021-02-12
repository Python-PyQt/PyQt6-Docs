.. sip:method-description::
    :status: todo
    :pysig: f1fc9d3b12410d466c565e28fc9d61a3
    :realsig: (qint64)
    :digest: 155aa39d7e96a86e1bbbfb689fe16206

Reads one line of text from the stream, and returns it as a QString. The maximum allowed line length is set to *maxlen*. If the stream contains lines longer than this, then the lines will be split after *maxlen* characters and returned in parts.

If *maxlen* is 0, the lines can be of any length.

The returned line has no trailing end-of-line characters ("\\n" or "\\r\\n"), so calling QString::trimmed() can be unnecessary.

If the stream has read to the end of the file,  will return a null QString. For strings, or for devices that support it, you can explicitly test for the end of the stream using :sip:ref:`~PyQt6.QtCore.QTextStream.atEnd`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTextStream.readAll`, :sip:ref:`~PyQt6.QtCore.QIODevice.readLine`.

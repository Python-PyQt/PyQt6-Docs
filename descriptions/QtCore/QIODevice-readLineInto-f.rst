.. sip:method-description::
    :status: todo
    :pysig: dcaae2de1e0bdc0616af83de27da8723
    :realsig: (QByteArray*, qint64)
    :digest: 0fd046f7949b84fe43da69e168a69e2f

Reads a line from the device, but no more than *maxSize* characters. and stores it as a byte array in *line*.

**Note:** Reads a line from this device even if *line* is ``nullptr``.

If *maxSize* is 0 or not specified, the line can be of any length, thereby enabling unlimited reading.

The resulting line can have trailing end-of-line characters ("\\n" or "\\r\\n"), so calling :sip:ref:`~PyQt6.QtCore.QByteArray.trimmed` may be necessary.

If no data was currently available for reading, or in case an error occurred, this function returns ``false`` and sets *line* to :sip:ref:`~PyQt6.QtCore.QByteArray.isEmpty`. Otherwise it returns ``true``.

Note that the contents of *line* before the call are discarded in any case but its :sip:ref:`~PyQt6.QtCore.QByteArray.capacity` is never reduced.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QIODevice.readAll`, :sip:ref:`~PyQt6.QtCore.QIODevice.readLine`, QTextStream::readLineInto().

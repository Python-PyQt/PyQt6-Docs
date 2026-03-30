.. sip:method-description::
    :status: todo
    :pysig: 0cdc5d412f649d44caa46f23734b9496
    :realsig: (QByteArray*, qint64)
    :digest: 7f83d34aa8d167c492c699a398a0b3ed

Reads a line from the device, but no more than *maxSize* characters. and stores it as a byte array in *line*.

**Note:** Reads a line from this device even if *line* is ``nullptr``.

If *maxSize* is 0 or not specified, the line can be of any length, thereby enabling unlimited reading.

The resulting line can have trailing end-of-line characters ("``\n``" or "``\r````\n``"), so calling :sip:ref:`~PyQt6.QtCore.QByteArray.trimmed` may be necessary.

If no data was currently available for reading, or in case an error occurred, this function returns ``false`` and sets *line* to :sip:ref:`~PyQt6.QtCore.QByteArray.isEmpty`. Otherwise it returns ``true``.

Note that the contents of *line* before the call are discarded in any case but its :sip:ref:`~PyQt6.QtCore.QByteArray.capacity` is never reduced.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QIODevice.readAll`, :sip:ref:`~PyQt6.QtCore.QIODevice.readLine`, QTextStream::readLineInto().

.. sip:method-description::
    :status: todo
    :pysig: 35be435d5eb927e68aeed4ae67cd8a52
    :realsig: (qint64)
    :digest: db5e375f23e3d23dd1663931a00f136c

Reads a line from the device, but no more than *maxSize* characters, and returns the result as a byte array.

If *maxSize* is 0 or not specified, the line can be of any length, thereby enabling unlimited reading.

The resulting line can have trailing end-of-line characters ("\\n" or "\\r\\n"), so calling :sip:ref:`~PyQt6.QtCore.QByteArray.trimmed` may be necessary.

This function has no way of reporting errors; returning an empty :sip:ref:`~PyQt6.QtCore.QByteArray` can mean either that no data was currently available for reading, or that an error occurred.

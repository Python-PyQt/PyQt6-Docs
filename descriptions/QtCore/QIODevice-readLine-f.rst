.. sip:method-description::
    :status: todo
    :pysig: 35be435d5eb927e68aeed4ae67cd8a52
    :realsig: (qint64)
    :digest: c6bd5e4c112de64197395a8300793294

This is an overloaded function.

Reads a line from the device, but no more than *maxSize* characters, and returns the result as a byte array.

This function has no way of reporting errors; returning an empty :sip:ref:`~PyQt6.QtCore.QByteArray` can mean either that no data was currently available for reading, or that an error occurred.

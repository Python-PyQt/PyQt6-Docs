.. sip:method-description::
    :status: todo
    :pysig: 35be435d5eb927e68aeed4ae67cd8a52
    :realsig: (qint64)
    :digest: 34cfb1e95de6b1e5ce1f6e691d2b6696

This is an overloaded function.

Reads at most *maxSize* bytes from the device, and returns the data read as a :sip:ref:`~PyQt6.QtCore.QByteArray`.

This function has no way of reporting errors; returning an empty :sip:ref:`~PyQt6.QtCore.QByteArray` can mean either that no data was currently available for reading, or that an error occurred.

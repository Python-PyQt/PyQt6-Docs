.. sip:method-description::
    :status: todo
    :pysig: 35be435d5eb927e68aeed4ae67cd8a52
    :realsig: (qint64)
    :digest: f1336f1456d4fba07bf1e5ae445a92dd

Reads at most *maxSize* bytes from the device, and returns the data read as a :sip:ref:`~PyQt6.QtCore.QByteArray`.

This function has no way of reporting errors; returning an empty :sip:ref:`~PyQt6.QtCore.QByteArray` can mean either that no data was currently available for reading, or that an error occurred.

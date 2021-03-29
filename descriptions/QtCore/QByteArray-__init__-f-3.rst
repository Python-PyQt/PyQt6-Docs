.. sip:method-description::
    :status: todo
    :pysig: f68a9646b4b9824d6ee155882d0b2050
    :realsig: (const char*,qsizetype)
    :digest: 7275ca4e4f73a3aaf70854da408a15ec

Constructs a byte array containing the first *size* bytes of array *data*.

If *data* is 0, a null byte array is constructed.

If *size* is negative, *data* is assumed to point to a '\\0'-terminated string and its length is determined dynamically.

:sip:ref:`~PyQt6.QtCore.QByteArray` makes a deep copy of the string data.

.. seealso:: fromRawData().

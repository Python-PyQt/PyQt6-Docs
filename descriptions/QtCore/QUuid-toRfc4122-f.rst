.. sip:method-description::
    :status: todo
    :pysig: a5704e7d57089c440a7d83c72d987b9e
    :realsig: () const
    :digest: 77ea17e33385513d8ad9d498b7c038f5

Returns the binary representation of this :sip:ref:`~PyQt6.QtCore.QUuid`. The byte array is in big endian format, and formatted according to RFC 4122, section 4.1.2 - "Layout and byte order".

The order is as follows:

+---------+----------------------+
| Field # | Source               |
+=========+======================+
| 1       | data1                |
+---------+----------------------+
| 2       | data2                |
+---------+----------------------+
| 3       | data3                |
+---------+----------------------+
| 4       | data4[0] .. data4[7] |
+---------+----------------------+

The bytes in the byte array returned by this function contains the same binary content as toBytes().

.. seealso:: toBytes().

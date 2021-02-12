.. sip:method-description::
    :status: todo
    :pysig: a5704e7d57089c440a7d83c72d987b9e
    :realsig: () const
    :digest: 91f07fc15cb5ed52aff35c3f72b85863

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

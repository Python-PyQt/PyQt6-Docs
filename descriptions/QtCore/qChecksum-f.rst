.. sip:method-description::
    :status: todo
    :pysig: a0f949892ff339348903935bcd4eafbf
    :realsig: (QByteArrayView,Qt::ChecksumType)
    :digest: f70eeaaf60791b08037b74ff19fc0627

Returns the CRC-16 checksum of *data*.

The checksum is independent of the byte order (endianness) and will be calculated accorded to the algorithm published in *standard*. By default the algorithm published in ISO 3309 (\ :sip:ref:`~PyQt6.QtCore.Qt.ChecksumType.ChecksumIso3309`) is used.

**Note:** This function is a 16-bit cache conserving (16 entry table) implementation of the CRC-16-CCITT algorithm.

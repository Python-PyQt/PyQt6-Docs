.. sip:method-description::
    :status: todo
    :pysig: edfc6ad7e4c99d0040585a75d6eaae73
    :realsig: (const QByteArray&)
    :digest: 227295dc9e76b7a0cabbcb3daa0047cf

Uncompresses the *data* byte array and returns a new byte array with the uncompressed data.

Returns an empty :sip:ref:`~PyQt6.QtCore.QByteArray` if the input data was corrupt.

This function will uncompress data compressed with :sip:ref:`~PyQt6.QtCore.qCompress` from this and any earlier Qt version, back to Qt 3.1 when this feature was added.

**Note:** If you want to use this function to uncompress external data that was compressed using zlib, you first need to prepend a four byte header to the byte array containing the data. The header must contain the expected length (in bytes) of the uncompressed data, expressed as an unsigned, big-endian, 32-bit integer.

.. seealso:: :sip:ref:`~PyQt6.QtCore.qCompress`.

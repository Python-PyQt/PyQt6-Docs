.. sip:method-description::
    :status: todo
    :pysig: b2cc0c4f8d9f710ef7e89ba9aa900aca
    :realsig: (const QByteArray&)
    :digest: e14d951556fe89bbfb66e88d2c65d8f5

Uncompresses the *data* byte array and returns a new byte array with the uncompressed data.

Returns an empty :sip:ref:`~PyQt6.QtCore.QByteArray` if the input data was corrupt.

This function will uncompress data compressed with :sip:ref:`~PyQt6.QtCore.qCompress` from this and any earlier Qt version, back to Qt 3.1 when this feature was added.

**Note:** If you want to use this function to uncompress external data that was compressed using zlib, you first need to prepend a four byte header to the byte array containing the data. The header must contain the expected length (in bytes) of the uncompressed data, expressed as an unsigned, big-endian, 32-bit integer. This number is just a hint for the initial size of the output buffer size, though. If the indicated size is too small to hold the result, the output buffer size will still be increased until either the output fits or the system runs out of memory. So, despite the 32-bit header, this function, on 64-bit platforms, can produce more than 4GiB of output.

**Note:** In Qt versions prior to Qt 6.5, more than 2GiB of data worked unreliably; in Qt versions prior to Qt 6.0, not at all.

.. seealso:: :sip:ref:`~PyQt6.QtCore.qCompress`.

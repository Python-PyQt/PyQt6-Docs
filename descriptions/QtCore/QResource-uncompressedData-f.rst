.. sip:method-description::
    :status: todo
    :pysig: a5704e7d57089c440a7d83c72d987b9e
    :realsig: () const
    :digest: 91b8e9123c1e9fdbcad30ec2487236e5

Returns the resource data, decompressing it first, if the data was stored compressed. If the resource is a directory or an error occurs while decompressing, a null :sip:ref:`~PyQt6.QtCore.QByteArray` is returned.

**Note:** If the data was compressed, this function will decompress every time it is called. The result is not cached between calls.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QResource.uncompressedSize`, :sip:ref:`~PyQt6.QtCore.QResource.size`, :sip:ref:`~PyQt6.QtCore.QResource.compressionAlgorithm`, :sip:ref:`~PyQt6.QtCore.QResource.isFile`.

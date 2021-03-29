.. sip:method-description::
    :status: todo
    :pysig: 4b3a6218bb3e3a7303e8a171a60fcf92
    :realsig: () const
    :digest: 62d5c976a80e6ca396d505ae4b63d0d3

Returns direct access to a segment of read-only data, that this resource represents. If the resource is compressed, the data returned is also compressed. The caller must then decompress the data or use :sip:ref:`~PyQt6.QtCore.QResource.uncompressedData`. If the resource is a directory, ``nullptr`` is returned.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QResource.uncompressedData`, :sip:ref:`~PyQt6.QtCore.QResource.size`, :sip:ref:`~PyQt6.QtCore.QResource.isFile`.

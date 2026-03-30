.. sip:method-description::
    :status: todo
    :pysig: d2780dadeffd828e55cb97abe0112dbb
    :realsig: () const
    :digest: e569f0ca6046758ddf71fc363655b893

The byte order of the pixel format determines the memory layout of the individual type units, as described by the :sip:ref:`~PyQt6.QtGui.QPixelFormat.typeInterpretation`.

This function will never return :sip:ref:`~PyQt6.QtGui.QPixelFormat.ByteOrder.CurrentSystemEndian` as this value is translated to the system's endian value in the constructor.

For pixel formats with :sip:ref:`~PyQt6.QtGui.QPixelFormat.typeInterpretation` :sip:ref:`~PyQt6.QtGui.QPixelFormat.TypeInterpretation.UnsignedByte` this will typically be :sip:ref:`~PyQt6.QtGui.QPixelFormat.ByteOrder.BigEndian`, while other type interpretations will typically reflect the endianness of the current system.

If the byte order of the pixel format matches the current system the individual type units can be read and manipulated using the same bit masks and operations, regardless of the host system endianness. For example, with :sip:ref:`~PyQt6.QtGui.QImage.Format.Format_ARGB32`, which has a :sip:ref:`~PyQt6.QtGui.QPixelFormat.TypeInterpretation.UnsignedInteger` type interpretation, the alpha can always be read by masking the ``unsigned int`` by ``0xFF000000``, regardless of the host endianness.

If the pixel format and host endianness does *not* match care must be taken to account for this. Classes like :sip:ref:`~PyQt6.QtGui.QImage` do not swap the internal bits to match the host system endianness in these cases.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPixelFormat.typeInterpretation`, :sip:ref:`~PyQt6.QtGui.QPixelFormat.alphaPosition`.

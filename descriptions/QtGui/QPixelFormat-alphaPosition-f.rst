.. sip:method-description::
    :status: todo
    :pysig: 6ada12c91359067667a4e7c5d4dc0549
    :realsig: () const
    :digest: 5f63e55dbbb28e25694f66e3e7692849

Accessor function for the position of the alpha channel relative to the color channels.

For formats where the individual channels map to individual units, the alpha position is relative to these units. For example for :sip:ref:`~PyQt6.QtGui.QImage.Format.Format_RGBA16FPx4` which has an alpha position of :sip:ref:`~PyQt6.QtGui.QPixelFormat.AlphaPosition.AtEnd`, the alpha is the last ``qfloat16`` read.

For formats where multiple channels are packed into a single unit, the :sip:ref:`~PyQt6.QtGui.QPixelFormat.AlphaPosition.AtBeginning` and :sip:ref:`~PyQt6.QtGui.QPixelFormat.AlphaPosition.AtEnd` values map to the most significant and least significant bits of the packed unit, with respect to the format's own :sip:ref:`~PyQt6.QtGui.QPixelFormat.byteOrder`.

For example, for :sip:ref:`~PyQt6.QtGui.QImage.Format.Format_ARGB32`, which has a type interpretation of :sip:ref:`~PyQt6.QtGui.QPixelFormat.TypeInterpretation.UnsignedInteger` and a :sip:ref:`~PyQt6.QtGui.QPixelFormat.byteOrder` that always matches the host system, the alpha position of :sip:ref:`~PyQt6.QtGui.QPixelFormat.AlphaPosition.AtBeginning` means that the alpha can always be found at ``0xFF000000``.

If the pixel format and host endianness does *not* match care must be taken to correctly map the pixel format layout to the host memory layout.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPixelFormat.alphaUsage`, :sip:ref:`~PyQt6.QtGui.QPixelFormat.alphaSize`, :sip:ref:`~PyQt6.QtGui.QPixelFormat.premultiplied`.

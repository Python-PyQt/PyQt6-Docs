.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 6548d537113bda22cf40516338f1e815

Returns the device position corresponding to the current position of the stream, or -1 if an error occurs (e.g., if there is no device or string, or if there's a device error).

Because :sip:ref:`~PyQt6.QtCore.QTextStream` is buffered, this function may have to seek the device to reconstruct a valid device position. This operation can be expensive, so you may want to avoid calling this function in a tight loop.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QTextStream.seek`.

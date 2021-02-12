.. sip:method-description::
    :status: todo
    :pysig: 4926f07c192a1c65319b6998bcf87ba4
    :realsig: (QDataStream::FloatingPointPrecision)
    :digest: c07b0790753bac5a048ffab4bd803de5

Sets the floating point precision of the data stream to *precision*. If the floating point precision is :sip:ref:`~PyQt6.QtCore.QDataStream.FloatingPointPrecision.DoublePrecision` and the version of the data stream is :sip:ref:`~PyQt6.QtCore.QDataStream.Version.Qt_4_6` or higher, all floating point numbers will be written and read with 64-bit precision. If the floating point precision is :sip:ref:`~PyQt6.QtCore.QDataStream.FloatingPointPrecision.SinglePrecision` and the version is :sip:ref:`~PyQt6.QtCore.QDataStream.Version.Qt_4_6` or higher, all floating point numbers will be written and read with 32-bit precision.

For versions prior to :sip:ref:`~PyQt6.QtCore.QDataStream.Version.Qt_4_6`, the precision of floating point numbers in the data stream depends on the stream operator called.

The default is :sip:ref:`~PyQt6.QtCore.QDataStream.FloatingPointPrecision.DoublePrecision`.

Note that this property does not affect the serialization or deserialization of ``qfloat16`` instances.

**Warning:** This property must be set to the same value on the object that writes and the object that reads the data stream.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDataStream.floatingPointPrecision`.

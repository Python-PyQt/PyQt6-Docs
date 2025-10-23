.. sip:method-description::
    :status: todo
    :pysig: a5704e7d57089c440a7d83c72d987b9e
    :realsig: ()
    :digest: 86f33752124407172851596be902b1dc

If this byte array's data isn't null-terminated, this method will make a deep-copy of the data and make it null-terminated.

A :sip:ref:`~PyQt6.QtCore.QByteArray` is null-terminated by default, however in some cases (e.g. when using fromRawData()), the data doesn't necessarily end with a ``\0`` character, which could be a problem when calling methods that expect a null-terminated string (for example, C API).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QByteArray.nullTerminated`, fromRawData(), setRawData().

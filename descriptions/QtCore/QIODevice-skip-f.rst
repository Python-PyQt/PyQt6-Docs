.. sip:method-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (qint64)
    :digest: 68ce9bc9e17f557e8603a127726b3470

Skips up to *maxSize* bytes from the device. Returns the number of bytes actually skipped, or -1 on error.

This function does not wait and only discards the data that is already available for reading.

If the device is opened in text mode, end-of-line terminators are translated to '\\n' symbols and count as a single byte identically to the :sip:ref:`~PyQt6.QtCore.QIODevice.read` and :sip:ref:`~PyQt6.QtCore.QIODevice.peek` behavior.

This function works for all devices, including sequential ones that cannot :sip:ref:`~PyQt6.QtCore.QIODevice.seek`. It is optimized to skip unwanted data after a :sip:ref:`~PyQt6.QtCore.QIODevice.peek` call.

For random-access devices, skip() can be used to seek forward from the current position. Negative *maxSize* values are not allowed.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QIODevice.skipData`, :sip:ref:`~PyQt6.QtCore.QIODevice.peek`, :sip:ref:`~PyQt6.QtCore.QIODevice.seek`, :sip:ref:`~PyQt6.QtCore.QIODevice.read`.

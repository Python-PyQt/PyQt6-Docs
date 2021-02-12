.. sip:method-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (int)
    :digest: 09615d15f7ffd35c6e2153a4e876a768

Skips *len* bytes from the device. Returns the number of bytes actually skipped, or -1 on error.

This is equivalent to calling :sip:ref:`~PyQt6.QtCore.QDataStream.readRawData` on a buffer of length *len* and ignoring the buffer.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QIODevice.seek`.

.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: 421f91ffe31747f4ce5cb07bd0a558eb

Sets the file descriptor that this :sip:ref:`~PyQt6.QtDBus.QDBusUnixFileDescriptor` object holds to a copy of *fileDescriptor*. The original file descriptor is not touched and must be closed by the user.

Note that the value returned by :sip:ref:`~PyQt6.QtDBus.QDBusUnixFileDescriptor.fileDescriptor` will be different from the *fileDescriptor* parameter passed.

If the *fileDescriptor* parameter is not valid, :sip:ref:`~PyQt6.QtDBus.QDBusUnixFileDescriptor.isValid` will return false and :sip:ref:`~PyQt6.QtDBus.QDBusUnixFileDescriptor.fileDescriptor` will return -1.

.. seealso:: :sip:ref:`~PyQt6.QtDBus.QDBusUnixFileDescriptor.isValid`, :sip:ref:`~PyQt6.QtDBus.QDBusUnixFileDescriptor.fileDescriptor`.

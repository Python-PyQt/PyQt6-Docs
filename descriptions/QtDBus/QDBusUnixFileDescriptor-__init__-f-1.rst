.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: 3b5a93361029969aa16a4560c0dffe8b

Constructs a :sip:ref:`~PyQt6.QtDBus.QDBusUnixFileDescriptor` object by copying the *fileDescriptor* parameter. The original file descriptor is not touched and must be closed by the user.

Note that the value returned by :sip:ref:`~PyQt6.QtDBus.QDBusUnixFileDescriptor.fileDescriptor` will be different from the *fileDescriptor* parameter passed.

If the *fileDescriptor* parameter is not valid, :sip:ref:`~PyQt6.QtDBus.QDBusUnixFileDescriptor.isValid` will return false and :sip:ref:`~PyQt6.QtDBus.QDBusUnixFileDescriptor.fileDescriptor` will return -1.

.. seealso:: :sip:ref:`~PyQt6.QtDBus.QDBusUnixFileDescriptor.setFileDescriptor`, :sip:ref:`~PyQt6.QtDBus.QDBusUnixFileDescriptor.fileDescriptor`.

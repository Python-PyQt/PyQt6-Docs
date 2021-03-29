.. sip:method-description::
    :status: todo
    :pysig: 01111d32dddd979ac6254452ab6fef9b
    :realsig: ()
    :digest: d7ad3dabb0ac169230e7089b28d58605

Returns ``true`` if Unix file descriptors are supported on this platform. In other words, this function returns ``true`` if this is a Unix platform.

Note that :sip:ref:`~PyQt6.QtDBus.QDBusUnixFileDescriptor` continues to operate even if this function returns ``false``. The only difference is that the :sip:ref:`~PyQt6.QtDBus.QDBusUnixFileDescriptor` objects will always be in the :sip:ref:`~PyQt6.QtDBus.QDBusUnixFileDescriptor.isValid` == false state and :sip:ref:`~PyQt6.QtDBus.QDBusUnixFileDescriptor.fileDescriptor` will always return -1. The class will not consume any operating system resources.

.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 9f2f5689163b2a14e605f352688a4018

Returns the Unix file descriptor contained by this :sip:ref:`~PyQt6.QtDBus.QDBusUnixFileDescriptor` object. An invalid file descriptor is represented by the value -1.

Note that the file descriptor returned by this function is owned by the :sip:ref:`~PyQt6.QtDBus.QDBusUnixFileDescriptor` object and must not be stored past the lifetime of this object. It is ok to use it while this object is valid, but if one wants to store it for longer use, the file descriptor should be cloned using the Unix ``dup(2)``, ``dup2(2)`` or ``dup3(2)`` functions.

.. seealso:: :sip:ref:`~PyQt6.QtDBus.QDBusUnixFileDescriptor.setFileDescriptor`, :sip:ref:`~PyQt6.QtDBus.QDBusUnixFileDescriptor.isValid`.

.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: b2d509548fd3ae394918d90bbd8ec3cf

Returns the file handle of the file.

This is a small positive integer, suitable for use with C library functions such as ``fdopen()`` and ``fcntl()``. On systems that use file descriptors for sockets (i.e. Unix systems, but not Windows) the handle can be used with :sip:ref:`~PyQt6.QtCore.QSocketNotifier` as well.

If the file is not open, or there is an error, handle() returns -1.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSocketNotifier`.

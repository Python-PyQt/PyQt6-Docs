.. sip:method-description::
    :status: todo
    :pysig: 49cd6c4846645627c7c8750fdcfb2bfd
    :realsig: ()
    :digest: 1563e9c751a7db9544b519bf7b3095c1

Returns the type of the operating system kernel Qt was compiled for. It's also the kernel the application is running on, unless the host operating system is running a form of compatibility or virtualization layer.

Values returned by this function are stable and will not change over time, so applications can rely on the returned value as an identifier, except that new OS kernel types may be added over time.

On Windows, this function returns the type of Windows kernel, like "winnt". On Unix systems, it returns the same as the output of ``uname -s`` (lowercased).

**Note:** This function may return surprising values: it returns "linux" for all operating systems running Linux (including Android), "qnx" for all operating systems running QNX, "freebsd" for Debian/kFreeBSD, and "darwin" for macOS and iOS. For information on the type of product the application is running on, see :sip:ref:`~PyQt6.QtCore.QSysInfo.productType`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileSelector`, :sip:ref:`~PyQt6.QtCore.QSysInfo.kernelVersion`, :sip:ref:`~PyQt6.QtCore.QSysInfo.productType`, :sip:ref:`~PyQt6.QtCore.QSysInfo.productVersion`, :sip:ref:`~PyQt6.QtCore.QSysInfo.prettyProductName`.

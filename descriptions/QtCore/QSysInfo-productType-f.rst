.. sip:method-description::
    :status: todo
    :pysig: 49cd6c4846645627c7c8750fdcfb2bfd
    :realsig: ()
    :digest: f1a86535cd71534a8a0cbf8a35ed4c41

Returns the product name of the operating system this application is running in. If the application is running on some sort of emulation or virtualization layer (such as WINE on a Unix system), this function will inspect the emulation / virtualization layer.

Values returned by this function are stable and will not change over time, so applications can rely on the returned value as an identifier, except that new OS types may be added over time.

**Linux and Android note**: this function returns "android" for Linux systems running Android userspace, notably when using the Bionic library. For all other Linux systems, regardless of C library being used, it tries to determine the distribution name and returns that. If determining the distribution name failed, it returns "unknown".

**macOS note**: this function returns "macos" for all macOS systems, regardless of Apple naming convention. Previously, in Qt 5, it returned "osx", again regardless of Apple naming conventions.

**Darwin, iOS, tvOS, and watchOS note**: this function returns "ios" for iOS systems, "tvos" for tvOS systems, "watchos" for watchOS systems, and "darwin" in case the system could not be determined.

**FreeBSD note**: this function returns "debian" for Debian/kFreeBSD and "unknown" otherwise.

**Windows note**: this function return "windows"

**VxWorks note**: this function return "vxworks"

For other Unix-type systems, this function usually returns "unknown".

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFileSelector`, :sip:ref:`~PyQt6.QtCore.QSysInfo.kernelType`, :sip:ref:`~PyQt6.QtCore.QSysInfo.kernelVersion`, :sip:ref:`~PyQt6.QtCore.QSysInfo.productVersion`, :sip:ref:`~PyQt6.QtCore.QSysInfo.prettyProductName`.

.. sip:method-description::
    :status: todo
    :pysig: 49cd6c4846645627c7c8750fdcfb2bfd
    :realsig: ()
    :digest: 70888a35e192e4ff2a89fe4b1028e2a5

Returns the product version of the operating system in string form. If the version could not be determined, this function returns "unknown".

It will return the Android, iOS, macOS, VxWorks, Windows full-product versions on those systems.

Typical returned values are (note: list not exhaustive):

* "12" (Android 12)

* "36" (Fedora 36)

* "15.5" (iOS 15.5)

* "12.4" (macOS Monterey)

* "22.04" (Ubuntu 22.04)

* "8.6" (watchOS 8.6)

* "11" (Windows 11)

* "Server 2022" (Windows Server 2022)

* "24.03" (VxWorks 7 - 24.03)

On Linux systems, it will try to determine the distribution version and will return that. This is also done on Debian/kFreeBSD, so this function will return Debian version in that case.

In all other Unix-type systems, this function always returns "unknown".

**Note:** The version string returned from this function is not guaranteed to be orderable. On Linux, the version of the distribution may jump unexpectedly, please refer to the distribution's documentation for versioning practices.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSysInfo.kernelType`, :sip:ref:`~PyQt6.QtCore.QSysInfo.kernelVersion`, :sip:ref:`~PyQt6.QtCore.QSysInfo.productType`, :sip:ref:`~PyQt6.QtCore.QSysInfo.prettyProductName`.

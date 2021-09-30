.. sip:method-description::
    :status: todo
    :pysig: 49cd6c4846645627c7c8750fdcfb2bfd
    :realsig: ()
    :digest: 7d115a21b63a8f3d94d88e8259025236

Returns the product version of the operating system in string form. If the version could not be determined, this function returns "unknown".

It will return the Android, iOS, macOS, Windows full-product versions on those systems.

Typical returned values are (note: list not exhaustive):

* "2016.09" (Amazon Linux AMI 2016.09)

* "7.1" (Android Nougat)

* "25" (Fedora 25)

* "10.1" (iOS 10.1)

* "10.12" (macOS Sierra)

* "10.0" (tvOS 10)

* "16.10" (Ubuntu 16.10)

* "3.1" (watchOS 3.1)

* "10" (Windows 10)

* "Server 2016" (Windows Server 2016)

On Linux systems, it will try to determine the distribution version and will return that. This is also done on Debian/kFreeBSD, so this function will return Debian version in that case.

In all other Unix-type systems, this function always returns "unknown".

**Note:** The version string returned from this function is not guaranteed to be orderable. On Linux, the version of the distribution may jump unexpectedly, please refer to the distribution's documentation for versioning practices.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSysInfo.kernelType`, :sip:ref:`~PyQt6.QtCore.QSysInfo.kernelVersion`, :sip:ref:`~PyQt6.QtCore.QSysInfo.productType`, :sip:ref:`~PyQt6.QtCore.QSysInfo.prettyProductName`.

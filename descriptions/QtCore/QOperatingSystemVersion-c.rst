.. sip:class-description::
    :status: todo
    :brief: Information about the operating system version
    :digest: cfc4fd014b1a5564fdc79d8657c779c1

The :sip:ref:`~PyQt6.QtCore.QOperatingSystemVersion` class provides information about the operating system version.

Unlike other version functions in :sip:ref:`~PyQt6.QtCore.QSysInfo`, :sip:ref:`~PyQt6.QtCore.QOperatingSystemVersion` provides access to the full version number that *developers* typically use to vary behavior or determine whether to enable APIs or features based on the operating system version (as opposed to the kernel version number or marketing version).

Presently, Android, Apple Platforms (iOS, macOS, tvOS, and watchOS), and Windows are supported.

The *majorVersion()*, *minorVersion()*, and *microVersion()* functions return the parts of the operating system version number based on:

+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Platforms       | Value                                                                                                                                                                                                                                                                                                                                                                                              |
+=================+====================================================================================================================================================================================================================================================================================================================================================================================================+
| Android         | result of parsing `android.os.Build.VERSION.RELEASE <https://developer.android.com/reference/android/os/Build.VERSION.html#RELEASE>`_ using :sip:ref:`~PyQt6.QtCore.QVersionNumber`, with a fallback to `android.os.Build.VERSION.SDK_INT <https://developer.android.com/reference/android/os/Build.VERSION.html#SDK_INT>`_ to determine the major and minor version component if the former fails |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Apple Platforms | :sip:ref:`~PyQt6.QtCore.QOperatingSystemVersion.majorVersion`, :sip:ref:`~PyQt6.QtCore.QOperatingSystemVersion.minorVersion`, and patchVersion from `NSProcessInfo.operatingSystemVersion <https://developer.apple.com/reference/foundation/nsprocessinfo/1410906-operatingsystemversion?language=objc>`_                                                                                          |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Windows         | dwMajorVersion, dwMinorVersion, and dwBuildNumber from `RtlGetVersion <https://msdn.microsoft.com/en-us/library/mt723418.aspx>`_ - note that this function ALWAYS return the version number of the underlying operating system, as opposed to the shim underneath GetVersionEx that hides the real version number if the application is not manifested for that version of the OS                  |
+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Because :sip:ref:`~PyQt6.QtCore.QOperatingSystemVersion` stores both a version number and an OS type, the OS type can be taken into account when performing comparisons. For example, on a macOS system running macOS Sierra (v10.12), the following expression will return ``false`` even though the major version number component of the object on the left hand side of the expression (10) is greater than that of the object on the right (9):

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_global_qoperatingsystemversion.py
    :lines: 54-54

This allows expressions for multiple operating systems to be joined with a logical OR operator and still work as expected. For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_global_qoperatingsystemversion.py
    :lines: 58-62

A more naive comparison algorithm might incorrectly return true on all versions of macOS, including Mac OS 9. This behavior is achieved by overloading the comparison operators to return ``false`` whenever the OS types of the :sip:ref:`~PyQt6.QtCore.QOperatingSystemVersion` instances being compared do not match. Be aware that due to this it can be the case ``x`` >= y and ``x`` < y are BOTH ``false`` for the same instances of ``x`` and ``y``.

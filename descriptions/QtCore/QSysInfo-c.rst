.. sip:class-description::
    :status: todo
    :brief: Information about the system
    :digest: 2c4f217886700834d3832559f641b0cc

The :sip:ref:`~PyQt6.QtCore.QSysInfo` class provides information about the system.

* :sip:ref:`~PyQt6.QtCore.QSysInfo.Sizes.WordSize` specifies the size of a pointer for the platform on which the application is compiled.

* :sip:ref:`~PyQt6.QtCore.QSysInfo.Endian.ByteOrder` specifies whether the platform is big-endian or little-endian.

Some constants are defined only on certain platforms. You can use the preprocessor symbols Q_OS_WIN and Q_OS_MACOS to test that the application is compiled under Windows or macOS.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLibraryInfo`.

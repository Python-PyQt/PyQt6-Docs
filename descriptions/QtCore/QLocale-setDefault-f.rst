.. sip:method-description::
    :status: todo
    :pysig: beae116e6e30ff65b5adb869b565e847
    :realsig: (const QLocale&)
    :digest: 2eb2dd4395d55ba0060506681499e8c2

Sets the global default locale to *locale*. These values are used when a :sip:ref:`~PyQt6.QtCore.QLocale` object is constructed with no arguments. If this function is not called, the system's locale is used.

**Warning:** In a multithreaded application, the default locale should be set at application startup, before any non-GUI threads are created.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.system`, :sip:ref:`~PyQt6.QtCore.QLocale.c`.

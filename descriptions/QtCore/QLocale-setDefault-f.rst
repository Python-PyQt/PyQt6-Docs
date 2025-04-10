.. sip:method-description::
    :status: todo
    :pysig: beae116e6e30ff65b5adb869b565e847
    :realsig: (const QLocale&)
    :digest: 6e0f7e22fed99fe593a0d957f708a27c

Sets the global default locale to *locale*.

This locale is used when a :sip:ref:`~PyQt6.QtCore.QLocale` object is constructed with no arguments. If this function is not called, the system's locale is used.

**Warning:** In a multithreaded application, the default locale should be set at application startup, before any non-GUI threads are created.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.system`, :sip:ref:`~PyQt6.QtCore.QLocale.c`.

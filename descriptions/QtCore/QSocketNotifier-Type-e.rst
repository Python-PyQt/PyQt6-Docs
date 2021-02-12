.. sip:enum-description::
    :status: todo
    :digest: 58370284bd3a1a52695ab7e18c9a9cf5

This enum describes the various types of events that a socket notifier can recognize. The type must be specified when constructing the socket notifier.

Note that if you need to monitor both reads and writes for the same file descriptor, you must create two socket notifiers. Note also that it is not possible to install two socket notifiers of the same type (Read, Write, Exception) on the same socket.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSocketNotifier`, :sip:ref:`~PyQt6.QtCore.QSocketNotifier.type`.

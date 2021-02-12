.. sip:class-description::
    :status: todo
    :brief: Support for monitoring activity on a file descriptor
    :digest: c9a3a7a941ca051ed6e58f2d4555f003

The :sip:ref:`~PyQt6.QtCore.QSocketNotifier` class provides support for monitoring activity on a file descriptor.

The :sip:ref:`~PyQt6.QtCore.QSocketNotifier` makes it possible to integrate Qt's event loop with other event loops based on file descriptors. File descriptor action is detected in Qt's main event loop (\ :sip:ref:`~PyQt6.QtCore.QCoreApplication.exec`).

.. _qsocketnotifier-write-notifiers:

Once you have opened a device using a low-level (usually platform-specific) API, you can create a socket notifier to monitor the file descriptor. The socket notifier is enabled by default, i.e. it emits the :sip:ref:`~PyQt6.QtCore.QSocketNotifier.activated` signal whenever a socket event corresponding to its type occurs. Connect the :sip:ref:`~PyQt6.QtCore.QSocketNotifier.activated` signal to the slot you want to be called when an event corresponding to your socket notifier's type occurs.

There are three types of socket notifiers: read, write, and exception. The type is described by the :sip:ref:`~PyQt6.QtCore.QSocketNotifier.Type.Type` enum, and must be specified when constructing the socket notifier. After construction it can be determined using the :sip:ref:`~PyQt6.QtCore.QSocketNotifier.type` function. Note that if you need to monitor both reads and writes for the same file descriptor, you must create two socket notifiers. Note also that it is not possible to install two socket notifiers of the same type (\ :sip:ref:`~PyQt6.QtCore.QSocketNotifier.Type.Read`, :sip:ref:`~PyQt6.QtCore.QSocketNotifier.Type.Write`, :sip:ref:`~PyQt6.QtCore.QSocketNotifier.Type.Exception`) on the same socket.

The :sip:ref:`~PyQt6.QtCore.QSocketNotifier.setEnabled` function allows you to disable as well as enable the socket notifier. It is generally advisable to explicitly enable or disable the socket notifier, especially for write notifiers. A disabled notifier ignores socket events (the same effect as not creating the socket notifier). Use the :sip:ref:`~PyQt6.QtCore.QSocketNotifier.isEnabled` function to determine the notifier's current status.

Finally, you can use the :sip:ref:`~PyQt6.QtCore.QSocketNotifier.socket` function to retrieve the socket identifier. Although the class is called :sip:ref:`~PyQt6.QtCore.QSocketNotifier`, it is normally used for other types of devices than sockets. QTcpSocket and QUdpSocket provide notification through signals, so there is normally no need to use a :sip:ref:`~PyQt6.QtCore.QSocketNotifier` on them.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QFile`, `QProcess <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qprocess>`_.

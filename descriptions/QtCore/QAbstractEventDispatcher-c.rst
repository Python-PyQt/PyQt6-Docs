.. sip:class-description::
    :status: todo
    :brief: Interface to manage Qt's event queue
    :digest: cb11d33f2cfe243f85e1dc19f5beb10e

The :sip:ref:`~PyQt6.QtCore.QAbstractEventDispatcher` class provides an interface to manage Qt's event queue.

An event dispatcher receives events from the window system and other sources. It then sends them to the :sip:ref:`~PyQt6.QtCore.QCoreApplication` or :sip:ref:`~PyQt6.QtWidgets.QApplication` instance for processing and delivery. :sip:ref:`~PyQt6.QtCore.QAbstractEventDispatcher` provides fine-grained control over event delivery.

For simple control of event processing use :sip:ref:`~PyQt6.QtCore.QCoreApplication.processEvents`.

For finer control of the application's event loop, call :sip:ref:`~PyQt6.QtCore.QAbstractEventDispatcher.instance` and call functions on the :sip:ref:`~PyQt6.QtCore.QAbstractEventDispatcher` object that is returned. If you want to use your own instance of :sip:ref:`~PyQt6.QtCore.QAbstractEventDispatcher` or of a :sip:ref:`~PyQt6.QtCore.QAbstractEventDispatcher` subclass, you must install it with :sip:ref:`~PyQt6.QtCore.QCoreApplication.setEventDispatcher` or :sip:ref:`~PyQt6.QtCore.QThread.setEventDispatcher` *before* a default event dispatcher has been installed.

The main event loop is started by calling :sip:ref:`~PyQt6.QtCore.QCoreApplication.exec`, and stopped by calling :sip:ref:`~PyQt6.QtCore.QCoreApplication.exit`. Local event loops can be created using :sip:ref:`~PyQt6.QtCore.QEventLoop`.

Programs that perform long operations can call :sip:ref:`~PyQt6.QtCore.QAbstractEventDispatcher.processEvents` with a bitwise OR combination of various :sip:ref:`~PyQt6.QtCore.QEventLoop.ProcessEventFlags` values to control which events should be delivered.

:sip:ref:`~PyQt6.QtCore.QAbstractEventDispatcher` also allows the integration of an external event loop with the Qt event loop.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QEventLoop`, :sip:ref:`~PyQt6.QtCore.QCoreApplication`, :sip:ref:`~PyQt6.QtCore.QThread`.

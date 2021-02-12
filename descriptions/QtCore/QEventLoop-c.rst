.. sip:class-description::
    :status: todo
    :brief: Means of entering and leaving an event loop
    :digest: 9ebb5a79da2ae0e39a5d33ed3c48de8d

The :sip:ref:`~PyQt6.QtCore.QEventLoop` class provides a means of entering and leaving an event loop.

At any time, you can create a :sip:ref:`~PyQt6.QtCore.QEventLoop` object and call :sip:ref:`~PyQt6.QtCore.QEventLoop.exec` on it to start a local event loop. From within the event loop, calling :sip:ref:`~PyQt6.QtCore.QEventLoop.exit` will force :sip:ref:`~PyQt6.QtCore.QEventLoop.exec` to return.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractEventDispatcher`.

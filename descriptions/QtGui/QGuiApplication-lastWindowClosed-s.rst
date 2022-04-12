.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 8d62b1359ed16ee1022f4b74ad3ec20d

This signal is emitted from :sip:ref:`~PyQt6.QtGui.QGuiApplication.exec` when the last visible `primary window <https://doc.qt.io/qt-6/application-windows.html#primary-and-secondary-windows>`_ (i.e. top level window with no transient parent) is closed.

By default, :sip:ref:`~PyQt6.QtGui.QGuiApplication` quits after this signal is emitted. This feature can be turned off by setting :sip:ref:`~PyQt6.QtGui.QGuiApplication.quitOnLastWindowClosed` to ``false``.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QWindow.close`, :sip:ref:`~PyQt6.QtGui.QWindow.isTopLevel`, :sip:ref:`~PyQt6.QtGui.QWindow.transientParent`.

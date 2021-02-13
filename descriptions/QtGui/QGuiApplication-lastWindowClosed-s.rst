.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: ea97059f3f63f2c67c58224928d83b3a

This signal is emitted from :sip:ref:`~PyQt6.QtGui.QGuiApplication.exec` when the last visible primary window (i.e. window with no parent) is closed.

By default, :sip:ref:`~PyQt6.QtGui.QGuiApplication` quits after this signal is emitted. This feature can be turned off by setting :sip:ref:`~PyQt6.QtGui.QGuiApplication.quitOnLastWindowClosed` to ``false``.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QWindow.close`, :sip:ref:`~PyQt6.QtGui.QWindow.isTopLevel`.

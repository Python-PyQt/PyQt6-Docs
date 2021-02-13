.. sip:signal-description::
    :status: todo
    :pysig: cfe16859dacf5bcde9d1572da80463ec
    :realsig: (QScreen*)
    :digest: 9813dc290ea3bdc91920c2e7332f985b

This signal is emitted whenever a *screen* is removed from the system. It provides an opportunity to manage the windows on the screen before Qt falls back to moving them to the primary screen.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QGuiApplication.screens`, :sip:ref:`~PyQt6.QtGui.QGuiApplication.screenAdded`, :sip:ref:`~PyQt6.QtCore.QObject.destroyed`, :sip:ref:`~PyQt6.QtGui.QWindow.setScreen`.

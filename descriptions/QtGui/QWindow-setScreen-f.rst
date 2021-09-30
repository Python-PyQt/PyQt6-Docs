.. sip:method-description::
    :status: todo
    :pysig: cfe16859dacf5bcde9d1572da80463ec
    :realsig: (QScreen*)
    :digest: a548856f8f2262551f03995ca01f454d

Sets the screen on which the window should be shown.

If the window has been created, it will be recreated on the *newScreen*.

**Note:** If the screen is part of a virtual desktop of multiple screens, the window will not move automatically to *newScreen*. To place the window relative to the screen, use the screen's `topLeft() <https://doc.qt.io/qt-6/qml-georectangle.html#topleft>`_ position.

This function only works for top level windows.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QWindow.screen`, :sip:ref:`~PyQt6.QtGui.QScreen.virtualSiblings`.

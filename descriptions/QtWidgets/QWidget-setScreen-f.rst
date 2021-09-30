.. sip:method-description::
    :status: todo
    :pysig: cfe16859dacf5bcde9d1572da80463ec
    :realsig: (QScreen*)
    :digest: a49c9bbc6ee89206f02d886ab3810845

Sets the screen on which the widget should be shown to *screen*.

Setting the screen only makes sense for windows. If necessary, the widget's window will get recreated on *screen*.

**Note:** If the screen is part of a virtual desktop of multiple screens, the window will not move automatically to *screen*. To place the window relative to the screen, use the screen's `topLeft() <https://doc.qt.io/qt-6/qml-georectangle.html#topleft>`_ position.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.screen`, :sip:ref:`~PyQt6.QtGui.QWindow.setScreen`.

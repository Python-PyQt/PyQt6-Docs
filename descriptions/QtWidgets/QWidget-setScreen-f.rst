.. sip:method-description::
    :status: todo
    :pysig: cfe16859dacf5bcde9d1572da80463ec
    :realsig: (QScreen*)
    :digest: 6ee07dffbd85382a1456f5784fb40555

Sets the screen on which the widget should be shown to *screen*.

Setting the screen only makes sense for windows. If necessary, the widget's window will get recreated on *screen*.

**Note:** If the screen is part of a virtual desktop of multiple screens, the window will not move automatically to *screen*. To place the window relative to the screen, use the screen's topLeft() position.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.screen`, :sip:ref:`~PyQt6.QtGui.QWindow.setScreen`.

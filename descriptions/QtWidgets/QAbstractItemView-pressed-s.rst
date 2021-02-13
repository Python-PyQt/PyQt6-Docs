.. sip:signal-description::
    :status: todo
    :pysig: af193f7da54d4df813f044d1a85c747b
    :realsig: (const QModelIndex&)
    :digest: 6521d9047601f1667856959418142ff1

This signal is emitted when a mouse button is pressed. The item the mouse was pressed on is specified by *index*. The signal is only emitted when the index is valid.

Use the :sip:ref:`~PyQt6.QtGui.QGuiApplication.mouseButtons` function to get the state of the mouse buttons.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.activated`, :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.clicked`, :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.doubleClicked`, :sip:ref:`~PyQt6.QtWidgets.QAbstractItemView.entered`.

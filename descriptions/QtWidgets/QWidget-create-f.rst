.. sip:method-description::
    :status: todo
    :pysig: 5706dd9ed7169e498fa98c2c60247a79
    :realsig: (WId,bool,bool)
    :digest: 89211d45136a4a96c62fc416acb34088

Creates a new widget window.

The parameters *window*, *initializeWindow*, and *destroyOldWindow* are ignored in Qt 5. Please use :sip:ref:`~PyQt6.QtGui.QWindow.fromWinId` to create a :sip:ref:`~PyQt6.QtGui.QWindow` wrapping a foreign window and pass it to :sip:ref:`~PyQt6.QtWidgets.QWidget.createWindowContainer` instead.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.createWindowContainer`, :sip:ref:`~PyQt6.QtGui.QWindow.fromWinId`.

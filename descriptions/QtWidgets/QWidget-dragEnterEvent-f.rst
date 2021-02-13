.. sip:method-description::
    :status: todo
    :pysig: 8708b1d9b8a1d0e5467b1ef89589d7cc
    :realsig: (QDragEnterEvent*)
    :digest: 97acbb6eb63c688c6fddf1dd846bc49f

This event handler is called when a drag is in progress and the mouse enters this widget. The event is passed in the *event* parameter.

If the event is ignored, the widget won't receive any :sip:ref:`~PyQt6.QtWidgets.QWidget.dragMoveEvent`.

See the `Drag-and-drop documentation <https://doc.qt.io/qt-6/dnd.html>`_ for an overview of how to provide drag-and-drop in your application.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QDrag`, :sip:ref:`~PyQt6.QtGui.QDragEnterEvent`.

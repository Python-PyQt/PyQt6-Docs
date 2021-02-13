.. sip:method-description::
    :status: todo
    :pysig: c956f297e3f17e0e0de95e2e5b46c3ee
    :realsig: (QResizeEvent*)
    :digest: 1c9f6eab17987b5e5788167822385fb2

This event handler can be reimplemented in a subclass to receive widget resize events which are passed in the *event* parameter. When  is called, the widget already has its new geometry. The old size is accessible through :sip:ref:`~PyQt6.QtGui.QResizeEvent.oldSize`.

The widget will be erased and receive a paint event immediately after processing the resize event. No drawing need be (or should be) done inside this handler.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.moveEvent`, :sip:ref:`~PyQt6.QtWidgets.QWidget.event`, :sip:ref:`~PyQt6.QtWidgets.QWidget.resize`, :sip:ref:`~PyQt6.QtGui.QResizeEvent`, :sip:ref:`~PyQt6.QtWidgets.QWidget.paintEvent`, `Scribble Example <https://doc.qt.io/qt-6/qtwidgets-widgets-scribble-example.html>`_.

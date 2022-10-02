.. sip:method-description::
    :status: todo
    :pysig: 68829d2eb99d1d58831af2a1eab8e0c2
    :realsig: (QMouseEvent*)
    :digest: 4a02259b648115b26c0a8e92a10c0933

This event handler, for event *event*, can be reimplemented in a subclass to receive mouse press events for the widget.

If you create new widgets in the mousePressEvent() the :sip:ref:`~PyQt6.QtWidgets.QWidget.mouseReleaseEvent` may not end up where you expect, depending on the underlying window system (or X11 window manager), the widgets' location and maybe more.

The default implementation implements the closing of popup widgets when you click outside the window. For other widget types it does nothing.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.mouseReleaseEvent`, :sip:ref:`~PyQt6.QtWidgets.QWidget.mouseDoubleClickEvent`, :sip:ref:`~PyQt6.QtWidgets.QWidget.mouseMoveEvent`, :sip:ref:`~PyQt6.QtWidgets.QWidget.event`, :sip:ref:`~PyQt6.QtGui.QMouseEvent`, `Scribble Example <https://doc.qt.io/qt-6/qtwidgets-widgets-scribble-example.html>`_.

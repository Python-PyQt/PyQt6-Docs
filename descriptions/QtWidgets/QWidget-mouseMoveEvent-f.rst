.. sip:method-description::
    :status: todo
    :pysig: 68829d2eb99d1d58831af2a1eab8e0c2
    :realsig: (QMouseEvent*)
    :digest: e342b8ee64e549de1d31a6cbe5351a4a

This event handler, for event *event*, can be reimplemented in a subclass to receive mouse move events for the widget.

If mouse tracking is switched off, mouse move events only occur if a mouse button is pressed while the mouse is being moved. If mouse tracking is switched on, mouse move events occur even if no mouse button is pressed.

:sip:ref:`~PyQt6.QtGui.QMouseEvent.pos` reports the position of the mouse cursor, relative to this widget. For press and release events, the position is usually the same as the position of the last mouse move event, but it might be different if the user's hand shakes. This is a feature of the underlying window system, not Qt.

If you want to show a tooltip immediately, while the mouse is moving (e.g., to get the mouse coordinates with :sip:ref:`~PyQt6.QtGui.QMouseEvent.pos` and show them as a tooltip), you must first enable mouse tracking as described above. Then, to ensure that the tooltip is updated immediately, you must call :sip:ref:`~PyQt6.QtWidgets.QToolTip.showText` instead of :sip:ref:`~PyQt6.QtWidgets.QWidget.setToolTip` in your implementation of mouseMoveEvent().

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.setMouseTracking`, :sip:ref:`~PyQt6.QtWidgets.QWidget.mousePressEvent`, :sip:ref:`~PyQt6.QtWidgets.QWidget.mouseReleaseEvent`, :sip:ref:`~PyQt6.QtWidgets.QWidget.mouseDoubleClickEvent`, :sip:ref:`~PyQt6.QtWidgets.QWidget.event`, :sip:ref:`~PyQt6.QtGui.QMouseEvent`, `Scribble Example <https://doc.qt.io/qt-6/qtwidgets-widgets-scribble-example.html>`_.

.. sip:method-description::
    :status: todo
    :pysig: 68829d2eb99d1d58831af2a1eab8e0c2
    :realsig: (QMouseEvent*)
    :digest: e13de7814e0ea8f01ec8373adb986183

This event handler, for event *event*, can be reimplemented in a subclass to receive mouse double click events for the widget.

The default implementation calls :sip:ref:`~PyQt6.QtWidgets.QWidget.mousePressEvent`.

**Note:** The widget will also receive mouse press and mouse release events in addition to the double click event. And if another widget that overlaps this widget disappears in response to press or release events, then this widget will only receive the double click event. It is up to the developer to ensure that the application interprets these events correctly.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.mousePressEvent`, :sip:ref:`~PyQt6.QtWidgets.QWidget.mouseReleaseEvent`, :sip:ref:`~PyQt6.QtWidgets.QWidget.mouseMoveEvent`, :sip:ref:`~PyQt6.QtWidgets.QWidget.event`, :sip:ref:`~PyQt6.QtGui.QMouseEvent`.

.. sip:method-description::
    :status: todo
    :pysig: cc200f3284a058eeb2c0be78dd80207f
    :realsig: (QMoveEvent*)
    :digest: 2037dd4665d4f1332419fe886f5ccd4c

This event handler can be reimplemented in a subclass to receive widget move events which are passed in the *event* parameter. When the widget receives this event, it is already at the new position.

The old position is accessible through :sip:ref:`~PyQt6.QtGui.QMoveEvent.oldPos`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.resizeEvent`, :sip:ref:`~PyQt6.QtWidgets.QWidget.event`, :sip:ref:`~PyQt6.QtWidgets.QWidget.move`, :sip:ref:`~PyQt6.QtGui.QMoveEvent`.

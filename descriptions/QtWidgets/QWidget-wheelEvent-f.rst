.. sip:method-description::
    :status: todo
    :pysig: 58995d85e234d10a99bb87cdf1d979c9
    :realsig: (QWheelEvent*)
    :digest: 5a0b4f46967f4826fdc584a3da8f03df

This event handler, for event *event*, can be reimplemented in a subclass to receive wheel events for the widget.

If you reimplement this handler, it is very important that you :sip:ref:`~PyQt6.QtCore.QEvent` the event if you do not handle it, so that the widget's parent can interpret it.

The default implementation ignores the event.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QEvent.ignore`, :sip:ref:`~PyQt6.QtCore.QEvent.accept`, :sip:ref:`~PyQt6.QtWidgets.QWidget.event`, :sip:ref:`~PyQt6.QtGui.QWheelEvent`.

.. sip:method-description::
    :status: todo
    :pysig: 1892efa11dcd6bbbb9a3c11f9e2fe516
    :realsig: (QInputMethodEvent*)
    :digest: 7ca4fb5c979f51b6fcd16e939abc76ef

This event handler, for event *event*, can be reimplemented in a subclass to receive Input Method composition events. This handler is called when the state of the input method changes.

Note that when creating custom text editing widgets, the :sip:ref:`~PyQt6.QtCore.Qt.WidgetAttribute.WA_InputMethodEnabled` window attribute must be set explicitly (using the :sip:ref:`~PyQt6.QtWidgets.QWidget.setAttribute` function) in order to receive input method events.

The default implementation calls event->ignore(), which rejects the Input Method event. See the :sip:ref:`~PyQt6.QtGui.QInputMethodEvent` documentation for more details.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.event`, :sip:ref:`~PyQt6.QtGui.QInputMethodEvent`.

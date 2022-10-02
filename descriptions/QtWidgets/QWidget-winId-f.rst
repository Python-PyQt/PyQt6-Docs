.. sip:method-description::
    :status: todo
    :pysig: 4ace415a94e978d871810e1b2f0597f3
    :realsig: () const
    :digest: 86088f493e3c2f9cdbb47076ce465a36

Returns the window system identifier of the widget.

Portable in principle, but if you use it you are probably about to do something non-portable. Be careful.

If a widget is non-native (alien) and winId() is invoked on it, that widget will be provided a native handle.

This value may change at run-time. An event with type :sip:ref:`~PyQt6.QtCore.QEvent.Type.WinIdChange` will be sent to the widget following a change in window system identifier.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.find`.

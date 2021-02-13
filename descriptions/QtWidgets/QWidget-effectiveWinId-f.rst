.. sip:method-description::
    :status: todo
    :pysig: 4ace415a94e978d871810e1b2f0597f3
    :realsig: () const
    :digest: 03b61da8e136579a4776ec6fe42f67cd

Returns the effective window system identifier of the widget, i.e. the native parent's window system identifier.

If the widget is native, this function returns the native widget ID. Otherwise, the window ID of the first native parent widget, i.e., the top-level widget that contains this widget, is returned.

**Note:** We recommend that you do not store this value as it is likely to change at run-time.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.nativeParentWidget`.

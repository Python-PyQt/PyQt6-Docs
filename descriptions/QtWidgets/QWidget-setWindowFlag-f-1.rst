.. sip:method-description::
    :status: todo
    :pysig: 49bff4f604d53d1764edb1cbfe211327
    :realsig: (Qt::WindowType,bool)
    :digest: 4a3ac03b7e2ff078ca7663f3c6ca2df8

Sets the window flag *flag* on this widget if *on* is true; otherwise clears the flag.

**Note:** This function calls :sip:ref:`~PyQt6.QtWidgets.QWidget.setParent` when changing the flags for a window, causing the widget to be hidden. You must call :sip:ref:`~PyQt6.QtWidgets.QWidget.show` to make the widget visible again.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.setWindowFlags`, :sip:ref:`~PyQt6.QtWidgets.QWidget.windowFlags`, :sip:ref:`~PyQt6.QtWidgets.QWidget.windowType`.

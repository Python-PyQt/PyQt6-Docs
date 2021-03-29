.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 9db1000350d89434a17bea6889fa4a6b

Takes keyboard input focus from the widget.

If the widget has active focus, a :sip:ref:`~PyQt6.QtWidgets.QWidget.focusOutEvent` is sent to this widget to tell it that it has lost the focus.

This widget must enable focus setting in order to get the keyboard input focus, i.e. it must call :sip:ref:`~PyQt6.QtWidgets.QWidget.setFocusPolicy`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.hasFocus`, :sip:ref:`~PyQt6.QtWidgets.QWidget.setFocus`, :sip:ref:`~PyQt6.QtWidgets.QWidget.focusInEvent`, :sip:ref:`~PyQt6.QtWidgets.QWidget.focusOutEvent`, :sip:ref:`~PyQt6.QtWidgets.QWidget.setFocusPolicy`, :sip:ref:`~PyQt6.QtWidgets.QApplication.focusWidget`.

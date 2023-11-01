.. sip:method-description::
    :status: todo
    :pysig: 5a6e30521ff6150b2e0a693194e10d98
    :realsig: ()
    :digest: 6db95fb67e45c15a41e16b851564c532

Returns the application top-level window that has the keyboard input focus, or ``nullptr`` if no application window has the focus. There might be an activeWindow() even if there is no :sip:ref:`~PyQt6.QtWidgets.QApplication.focusWidget`, for example if no widget in that window accepts key events.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.setFocus`, :sip:ref:`~PyQt6.QtWidgets.QWidget.hasFocus`, :sip:ref:`~PyQt6.QtWidgets.QApplication.focusWidget`.

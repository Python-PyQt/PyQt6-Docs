.. sip:method-description::
    :status: todo
    :pysig: 5a6e30521ff6150b2e0a693194e10d98
    :realsig: (QWidget*)
    :digest: 82793c438658d954344ac1603eb959c9

Use :sip:ref:`~PyQt6.QtWidgets.QWidget.activateWindow` instead.

Sets the active window to the *active* widget in response to a system event. The function is called from the platform specific event handlers.

**Warning:** This function does *not* set the keyboard focus to the active widget. Call :sip:ref:`~PyQt6.QtWidgets.QWidget.activateWindow` instead.

It sets the :sip:ref:`~PyQt6.QtWidgets.QApplication.activeWindow` and :sip:ref:`~PyQt6.QtWidgets.QApplication.focusWidget` attributes and sends proper :sip:ref:`~PyQt6.QtCore.QEvent.Type.WindowActivate`/\ :sip:ref:`~PyQt6.QtCore.QEvent.Type.WindowDeactivate` and :sip:ref:`~PyQt6.QtCore.QEvent.Type.FocusIn`/\ :sip:ref:`~PyQt6.QtCore.QEvent.Type.FocusOut` events to all appropriate widgets. The window will then be painted in active state (e.g. cursors in line edits will blink), and it will have tool tips enabled.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QApplication.activeWindow`, :sip:ref:`~PyQt6.QtWidgets.QWidget.activateWindow`.

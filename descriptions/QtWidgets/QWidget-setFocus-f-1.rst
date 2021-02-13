.. sip:method-description::
    :status: todo
    :pysig: 8834a08c60caeffb04730243a04e173f
    :realsig: (Qt::FocusReason)
    :digest: f366b80c0ac6d04dc1d652205f101e9d

Gives the keyboard input focus to this widget (or its focus proxy) if this widget or one of its parents is the :sip:ref:`~PyQt6.QtWidgets.QWidget.isActiveWindow`. The *reason* argument will be passed into any focus event sent from this function, it is used to give an explanation of what caused the widget to get focus. If the window is not active, the widget will be given the focus when the window becomes active.

First, a focus about to change event is sent to the focus widget (if any) to tell it that it is about to lose the focus. Then focus is changed, a focus out event is sent to the previous focus item and a focus in event is sent to the new item to tell it that it just received the focus. (Nothing happens if the focus in and focus out widgets are the same.)

**Note:** On embedded platforms, :sip:ref:`~PyQt6.QtWidgets.QWidget.setFocus` will not cause an input panel to be opened by the input method. If you want this to happen, you have to send a :sip:ref:`~PyQt6.QtCore.QEvent.Type.RequestSoftwareInputPanel` event to the widget yourself.

:sip:ref:`~PyQt6.QtWidgets.QWidget.setFocus` gives focus to a widget regardless of its focus policy, but does not clear any keyboard grab (see :sip:ref:`~PyQt6.QtWidgets.QWidget.grabKeyboard`).

Be aware that if the widget is hidden, it will not accept focus until it is shown.

**Warning:** If you call :sip:ref:`~PyQt6.QtWidgets.QWidget.setFocus` in a function which may itself be called from :sip:ref:`~PyQt6.QtWidgets.QWidget.focusOutEvent` or :sip:ref:`~PyQt6.QtWidgets.QWidget.focusInEvent`, you may get an infinite recursion.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.hasFocus`, :sip:ref:`~PyQt6.QtWidgets.QWidget.clearFocus`, :sip:ref:`~PyQt6.QtWidgets.QWidget.focusInEvent`, :sip:ref:`~PyQt6.QtWidgets.QWidget.focusOutEvent`, :sip:ref:`~PyQt6.QtWidgets.QWidget.setFocusPolicy`, :sip:ref:`~PyQt6.QtWidgets.QWidget.focusWidget`, :sip:ref:`~PyQt6.QtWidgets.QApplication.focusWidget`, :sip:ref:`~PyQt6.QtWidgets.QWidget.grabKeyboard`, :sip:ref:`~PyQt6.QtWidgets.QWidget.grabMouse`, `Keyboard Focus in Widgets <https://doc.qt.io/qt-6/focus.html>`_, :sip:ref:`~PyQt6.QtCore.QEvent.Type.RequestSoftwareInputPanel`.

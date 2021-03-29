.. sip:method-description::
    :status: todo
    :pysig: a28d7c815182564df2c1abd853ad768a
    :realsig: (QFocusEvent*)
    :digest: e5982d129dbafc01689d37e87388dfda

This event handler can be reimplemented in a subclass to receive keyboard focus events (focus received) for the widget. The event is passed in the *event* parameter

A widget normally must :sip:ref:`~PyQt6.QtWidgets.QWidget.setFocusPolicy` to something other than :sip:ref:`~PyQt6.QtCore.Qt.FocusPolicy.NoFocus` in order to receive focus events. (Note that the application programmer can call :sip:ref:`~PyQt6.QtWidgets.QWidget.setFocus` on any widget, even those that do not normally accept focus.)

The default implementation updates the widget (except for windows that do not specify a :sip:ref:`~PyQt6.QtWidgets.QWidget.focusPolicy`).

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.focusOutEvent`, :sip:ref:`~PyQt6.QtWidgets.QWidget.setFocusPolicy`, :sip:ref:`~PyQt6.QtWidgets.QWidget.keyPressEvent`, :sip:ref:`~PyQt6.QtWidgets.QWidget.keyReleaseEvent`, :sip:ref:`~PyQt6.QtWidgets.QWidget.event`, :sip:ref:`~PyQt6.QtGui.QFocusEvent`.

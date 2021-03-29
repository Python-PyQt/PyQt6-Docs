.. sip:method-description::
    :status: todo
    :pysig: ce3d9b4daef6744486b5f293221f93ba
    :realsig: (QKeyEvent*)
    :digest: df5328d8be42648953e135ca6b1df9a3

This event handler, for event *event*, can be reimplemented in a subclass to receive key release events for the widget.

A widget must :sip:ref:`~PyQt6.QtWidgets.QWidget.setFocusPolicy` initially and :sip:ref:`~PyQt6.QtWidgets.QWidget.hasFocus` in order to receive a key release event.

If you reimplement this handler, it is very important that you call the base class implementation if you do not act upon the key.

The default implementation ignores the event, so that the widget's parent can interpret it.

Note that :sip:ref:`~PyQt6.QtGui.QKeyEvent` starts with isAccepted() == true, so you do not need to call QKeyEvent::accept() - just do not call the base class implementation if you act upon the key.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.keyPressEvent`, :sip:ref:`~PyQt6.QtCore.QEvent.ignore`, :sip:ref:`~PyQt6.QtWidgets.QWidget.setFocusPolicy`, :sip:ref:`~PyQt6.QtWidgets.QWidget.focusInEvent`, :sip:ref:`~PyQt6.QtWidgets.QWidget.focusOutEvent`, :sip:ref:`~PyQt6.QtWidgets.QWidget.event`, :sip:ref:`~PyQt6.QtGui.QKeyEvent`.

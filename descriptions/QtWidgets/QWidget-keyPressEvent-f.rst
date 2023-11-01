.. sip:method-description::
    :status: todo
    :pysig: ce3d9b4daef6744486b5f293221f93ba
    :realsig: (QKeyEvent*)
    :digest: ce613935d051704a8495fc193e81ea58

This event handler, for event *event*, can be reimplemented in a subclass to receive key press events for the widget.

A widget must call :sip:ref:`~PyQt6.QtWidgets.QWidget.setFocusPolicy` to accept focus initially and have focus in order to receive a key press event.

If you reimplement this handler, it is very important that you call the base class implementation if you do not act upon the key.

The default implementation closes popup widgets if the user presses the key sequence for :sip:ref:`~PyQt6.QtGui.QKeySequence.StandardKey.Cancel` (typically the Escape key). Otherwise the event is ignored, so that the widget's parent can interpret it.

Note that :sip:ref:`~PyQt6.QtGui.QKeyEvent` starts with isAccepted() == true, so you do not need to call QKeyEvent::accept() - just do not call the base class implementation if you act upon the key.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.keyReleaseEvent`, :sip:ref:`~PyQt6.QtWidgets.QWidget.setFocusPolicy`, :sip:ref:`~PyQt6.QtWidgets.QWidget.focusInEvent`, :sip:ref:`~PyQt6.QtWidgets.QWidget.focusOutEvent`, :sip:ref:`~PyQt6.QtWidgets.QWidget.event`, :sip:ref:`~PyQt6.QtGui.QKeyEvent`.

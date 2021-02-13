.. sip:method-description::
    :status: todo
    :pysig: d0c7c12c60c6b02dfcb8f6e6277451bf
    :realsig: (QCloseEvent*)
    :digest: 884857332022c23b9bd40c10cceb8710

Override this to handle close events (\ *ev*).

The function is called when the window is requested to close. Call :sip:ref:`~PyQt6.QtCore.QEvent.ignore` on the event if you want to prevent the window from being closed.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QWindow.close`.

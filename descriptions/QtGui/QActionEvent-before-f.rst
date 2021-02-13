.. sip:method-description::
    :status: todo
    :pysig: f8ca99b6c748ea427923a2f5f071f05b
    :realsig: () const
    :digest: 92c2dbd034f24b444dbeb6eb01a7e7f3

If type() is :sip:ref:`~PyQt6.QtCore.QEvent.Type.ActionAdded`, returns the action that should appear before :sip:ref:`~PyQt6.QtGui.QActionEvent.action`. If this function returns ``nullptr``, the action should be appended to already existing actions on the same widget.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QActionEvent.action`.

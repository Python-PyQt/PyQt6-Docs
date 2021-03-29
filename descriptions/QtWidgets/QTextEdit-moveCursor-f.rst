.. sip:method-description::
    :status: todo
    :pysig: c97bed08da9931ca32f402963fb588a7
    :realsig: (QTextCursor::MoveOperation,QTextCursor::MoveMode)
    :digest: 7bb4ddacf79a93f54ddbb4976856eaf8

Moves the cursor by performing the given *operation*.

If *mode* is :sip:ref:`~PyQt6.QtGui.QTextCursor.MoveMode.KeepAnchor`, the cursor selects the text it moves over. This is the same effect that the user achieves when they hold down the Shift key and move the cursor with the cursor keys.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextCursor.movePosition`.

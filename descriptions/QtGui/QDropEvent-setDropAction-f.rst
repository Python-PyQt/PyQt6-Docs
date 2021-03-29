.. sip:method-description::
    :status: todo
    :pysig: b730747ccdc682ff41f5a1b741c1a110
    :realsig: (Qt::DropAction)
    :digest: 63c791fcb8af17aec5a00dbf3146bb4d

Sets the *action* to be performed on the data by the target. Use this to override the :sip:ref:`~PyQt6.QtGui.QDropEvent.proposedAction` with one of the :sip:ref:`~PyQt6.QtGui.QDropEvent.possibleActions`.

If you set a drop action that is not one of the possible actions, the drag and drop operation will default to a copy operation.

Once you have supplied a replacement drop action, call accept() instead of :sip:ref:`~PyQt6.QtGui.QDropEvent.acceptProposedAction`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QDropEvent.dropAction`.

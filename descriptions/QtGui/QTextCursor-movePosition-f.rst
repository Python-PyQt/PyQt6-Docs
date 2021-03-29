.. sip:method-description::
    :status: todo
    :pysig: 3c104f0e39b7032136c09cd780c5e783
    :realsig: (QTextCursor::MoveOperation,QTextCursor::MoveMode,int)
    :digest: a908be17aa06d5aad3ba529fbe55fb0c

Moves the cursor by performing the given *operation* *n* times, using the specified *mode*, and returns ``true`` if all operations were completed successfully; otherwise returns ``false``.

For example, if this function is repeatedly used to seek to the end of the next word, it will eventually fail when the end of the document is reached.

By default, the move operation is performed once (\ *n* = 1).

If *mode* is ``KeepAnchor``, the cursor selects the text it moves over. This is the same effect that the user achieves when they hold down the Shift key and move the cursor with the cursor keys.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextCursor.setVisualNavigation`.

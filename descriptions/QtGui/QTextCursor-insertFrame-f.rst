.. sip:method-description::
    :status: todo
    :pysig: 4cad3b0364e71b42e96924be698e2ea4
    :realsig: (const QTextFrameFormat&)
    :digest: c4a20439dc9a8a06abfec40aecfa5739

Inserts a frame with the given *format* at the current cursor :sip:ref:`~PyQt6.QtGui.QTextCursor.position`, moves the cursor :sip:ref:`~PyQt6.QtGui.QTextCursor.position` inside the frame, and returns the frame.

If the cursor holds a selection, the whole selection is moved inside the frame.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextCursor.hasSelection`.

.. sip:signal-description::
    :status: todo
    :pysig: f4cc248e69b68bdc7c94b43874d7b9bd
    :realsig: (const QTextCursor&)
    :digest: 2e3080b4376faabd4fbd0b40dff7b3a7

This signal is emitted whenever the position of a cursor changed due to an editing operation. The cursor that changed is passed in *cursor*. If the document is used with the :sip:ref:`~PyQt6.QtWidgets.QTextEdit` class and you need a signal when the cursor is moved with the arrow keys you can use the :sip:ref:`~PyQt6.QtWidgets.QTextEdit.cursorPositionChanged` signal in :sip:ref:`~PyQt6.QtWidgets.QTextEdit`.

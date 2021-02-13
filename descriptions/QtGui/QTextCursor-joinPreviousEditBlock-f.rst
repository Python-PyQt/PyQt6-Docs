.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 906f016b4cd10e6e65910f650cbccc53

Like :sip:ref:`~PyQt6.QtGui.QTextCursor.beginEditBlock` indicates the start of a block of editing operations that should appear as a single operation for undo/redo. However unlike :sip:ref:`~PyQt6.QtGui.QTextCursor.beginEditBlock` it does not start a new block but reverses the previous call to :sip:ref:`~PyQt6.QtGui.QTextCursor.endEditBlock` and therefore makes following operations part of the previous edit block created.

For example:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_text_qtextcursor.py
    :lines: 94-106

The call to undo() will cause all three insertions to be undone.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextCursor.beginEditBlock`, :sip:ref:`~PyQt6.QtGui.QTextCursor.endEditBlock`.

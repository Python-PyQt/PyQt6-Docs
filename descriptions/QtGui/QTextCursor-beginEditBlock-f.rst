.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 8dced9217946890bebf036bb85370663

Indicates the start of a block of editing operations on the document that should appear as a single operation from an undo/redo point of view.

For example:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_text_qtextcursor.py
    :lines: 81-87

The call to undo() will cause both insertions to be undone, causing both "World" and "Hello" to be removed.

It is possible to nest calls to beginEditBlock and :sip:ref:`~PyQt6.QtGui.QTextCursor.endEditBlock`. The top-most pair will determine the scope of the undo/redo operation.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextCursor.endEditBlock`.

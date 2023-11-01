.. sip:method-description::
    :status: todo
    :pysig: 96e648b0c213feb955e3dc2c56751cf2
    :realsig: (const QString&)
    :digest: e9eb8540004f1ad17e1a2c1f00274eba

Inserts *text* at the current position, using the current character format.

If there is a selection, the selection is deleted and replaced by *text*, for example:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_text_qtextcursor.py
    :lines: 64-66

This clears any existing selection, selects the word at the cursor (i.e. from :sip:ref:`~PyQt6.QtGui.QTextCursor.position` forward), and replaces the selection with the phrase "Hello World".

Any ASCII linefeed characters (\\n) in the inserted text are transformed into unicode block separators, corresponding to :sip:ref:`~PyQt6.QtGui.QTextCursor.insertBlock` calls.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextCursor.charFormat`, :sip:ref:`~PyQt6.QtGui.QTextCursor.hasSelection`.

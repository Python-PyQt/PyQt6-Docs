.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: ff84b9df41ec8dcc80e3757df6288648

Returns the current selection's text (which may be empty). This only returns the text, with no rich text formatting information. If you want a document fragment (i.e. formatted rich text) use :sip:ref:`~PyQt6.QtGui.QTextCursor.selection` instead.

**Note:** If the selection obtained from an editor spans a line break, the text will contain a Unicode U+2029 paragraph separator character instead of a newline ``\n`` character. Use QString::replace() to replace these characters with newlines.
